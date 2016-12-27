
from django.utils.translation import ugettext_lazy as _
from django.contrib import auth
from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

import uuid
from rest_framework import generics, response, status, permissions, exceptions
from rest_framework.authtoken.models import Token

from .permissions import IsNotAuthenticated
from .models import Profile
from .serializers import (
    RegisterSerializer, LoginSerializer, LogOutSerializer, ProfileMiniSerializer,
    TokenSerializer, )


class Register(generics.CreateAPIView):
    """
    api to register user
    """
    serializer_class = RegisterSerializer
    permission_classes = (IsNotAuthenticated, )

    def create(self, request, format=None):
        serializer = self.get_serializer(data=request.data)

        error_data = {
            'message': _('Something went wrong. Please try again.'),
        }
        if serializer.is_valid():
            self.perform_create(request, serializer)
            response_data = {
                'message': _('User created and Activation Email sent successfully.'),
            }

            return response.Response(response_data, status=status.HTTP_201_CREATED)
        return response.Response(error_data, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, request, serializer):
        serializer.save()
        self.send_register_email(serializer.instance)

    def send_register_email(self, user):
        subject = "Account Activation Link"
        url = url = "https://peer.stg.gbci.org/?username="+user.username+"&activation-token="+str(user.uuid)
        context = {
            "url": url,
        }
        message = get_template("mail/acc_activation.html").render(Context(context))
        msg = EmailMessage(subject, message, to=[user.email, ], from_email="testit.roshan@gmail.com")
        msg.content_subtype = 'html'
        msg.send()


class ActionViewMixin(object):
    """
    Mixin to support busniess Actions in post
    instead of serializer save
    """
    def post(self, request):
        serializer = self.get_serializer(
            data=request.data)
        if serializer.is_valid():
            auth.login(request, serializer.instance)
            return self.action(serializer)
        else:
            return response.Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


class Login(ActionViewMixin, generics.GenericAPIView):

    """
    Use this endpoint to obtain user authentication token.
    """
    serializer_class = LoginSerializer
    permission_classes = (
        IsNotAuthenticated,
    )

    def finalize_response(self, request, *args, **kwargs):
        response_obj = super(Login, self).finalize_response(
            request, *args, **kwargs)
        if request.POST and response_obj.status_code == 200:
            response_obj['Authorization'] = 'Token '\
                + response_obj.data['auth_token']
            response_obj.set_cookie(
                'Authorization', response_obj['Authorization'])
        return response_obj

    def action(self, serializer):
        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)
        return response.Response(
            data=TokenSerializer(token).data,
            status=status.HTTP_200_OK,
        )


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
    lookup_url_kwarg = "username"
    lookup_field = "activation_key"

    def get(self, request, *args, **kwargs):
        print self.lookup_url_kwarg
        instance = get_object_or_404(self.model, username=self.kwargs[self.lookup_url_kwarg])
        if instance.uuid != uuid.UUID(self.kwargs[self.lookup_field]):
            raise exceptions.ParseError(_("Invalid Activation Token."))
        instance.account_activated = True
        instance.save()
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

    def get_queryset(self):
        print self.queryset
        if self.request.user.is_authenticated:
            return self.queryset.filter(username=self.request.user.username)
        return self.queryset


class GenerateCSRFToken(generics.GenericAPIView):
    """
    generate a csrf token
    """
    def get(self, request, *args, **kwargs):
        response_data = {
            "csrf": get_token(request)
        }
        return response.Response(response_data, status=status.HTTP_200_OK)
