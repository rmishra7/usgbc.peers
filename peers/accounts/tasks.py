from django.utils.translation import gettext_lazy as _
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib.sites.models import Site
from django.shortcuts import get_object_or_404

from celery import shared_task

from .models import Profile as User


@shared_task
def user_activation_listener(user):
    """
    Send Activation link to User to activate account
    """
    current_site = Site.objects.get_current()
    domain = unicode(current_site.domain)
    user = get_object_or_404(User, pk=user)
    subject = _("User Activation Email")
    ctx = {
        "user": user,
        "temp_key": user.uuid,
        "domain": domain,
    }
    message = get_template("accounts/tasks/user_activate.html").render(ctx)
    msg = EmailMessage(subject, message, to=[user.email])
    msg.content_subtype = "html"
    msg.send()
