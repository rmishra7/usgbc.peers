from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib.sites.models import Site
from django.shortcuts import get_object_or_404

from celery import shared_task

from .models import Profile as User


@shared_task
def project_submission_listener(user):
    """
    Send Password Reset link to User using temp_key generated
    """
    user = get_object_or_404(User, pk=user)
    subject = _("New project Submitted")
    ctx = {
        "user": user,
    }
    print settings.ADMINS
    message = get_template("projects/tasks/project_submission.html").render(ctx)
    msg = EmailMessage(subject, message, to=settings.ADMINS)
    msg.content_subtype = "html"
    msg.send()


@shared_task
def project_submission_success_listener(user):
    """
    Send Password Reset link to User using temp_key generated
    """
    user = get_object_or_404(User, pk=user)
    subject = _("Project Submission Success")
    ctx = {
        "user": user,
    }
    message = get_template("projects/tasks/project_submission_success.html").render(ctx)
    msg = EmailMessage(subject, message, to=[user.email])
    msg.content_subtype = "html"
    msg.send()
