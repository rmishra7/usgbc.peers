
from django.utils.translation import ugettext_lazy as _
from django.contrib import auth
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.sites.models import Site
from django.template.loader import get_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import uuid
import smtplib

from rest_framework import generics, response, status, permissions, exceptions, filters

from .permissions import IsNotAuthenticated
from .models import Profile
from .serializers import (
    RegisterSerializer, LoginSerializer, LogOutSerializer, ProfileMiniSerializer)
# from .tasks import user_activation_listener


class Register(generics.CreateAPIView):
    """
    api to register user
    """
    serializer_class = RegisterSerializer
    permission_classes = (IsNotAuthenticated, )

    def create(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            response_data = {
                'message': _('User created and Activation Email sent successfully.'),
            }
            return response.Response(response_data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()
        self.send_register_email(serializer.instance)
        # user_activation_listener.delay(serializer.instance.pk)
        # auth.login(self.request, serializer.instance)

    def send_register_email(self, user):
        sender = 'testit.roshan@gmail.com'
        sender_pass = 'initpass'
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "User Account Email"
        msg['From'] = sender
        msg['To'] = user.email
        to = [user.email, ]
        current_site = Site.objects.get_current()
        domain = unicode(current_site.domain)
        url = domain+"/auth/account/activate/"+user.username+"/"+str(user.uuid)+"/"
        text = '<h2><a href="'+url+'">Click here</a> to activate your account.</h2>'
        html = '<html><head></head><body><h2><a href="'+url+'">Click here</a> to activate your account.</h2></body></html>'
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(sender, sender_pass)
            server.sendmail(sender, to, msg.as_string())
            server.close()
            print 'Email sent!'
        except:
            print 'Something went wrong...'


class Login(generics.GenericAPIView):

    """
    Signin using your email address and password
    """
    serializer_class = LoginSerializer
    permission_classes = (IsNotAuthenticated, )

    def post(self, request, format=None):
        """
        Authenticate User againest credentials & return Authorization token
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            auth.login(request, serializer.instance)
            response_data = {
                'message': _('Logged in successfully'),
            }
            return response.Response(response_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOut(generics.GenericAPIView):
    """
    api to unauthenticate/logout the user
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = LogOutSerializer

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        response_data = {
            'message': _('Logged out successfully'),
        }
        return response.Response(response_data, status=status.HTTP_200_OK)


class UserActivation(generics.GenericAPIView):
    """
    api to activate user account and Authenticate the user
    """
    model = Profile
    permission_classes = (IsNotAuthenticated, )
    lookup_url_kwargs = "username"
    lookup_field = "activation_key"

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(self.model, username=self.kwargs[self.lookup_url_kwargs])
        if instance.uuid != uuid.UUID(self.kwargs[self.lookup_field]):
            raise exceptions.ParseError(_("Invalid Activation Token."))
        instance.account_activated = True
        instance.save()
        instance.backend = settings.AUTHENTICATION_BACKENDS[0]
        auth.login(self.request, instance)
        response_data = {
            'message': _('Account Activated Successfully.'),
        }
        return response.Response(response_data, status=status.HTTP_200_OK)


class UserList(generics.ListAPIView):
    """
    list of users based on search by first name
    """
    model = Profile
    serializer_class = ProfileMiniSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = model.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('first_name', 'last_name')
