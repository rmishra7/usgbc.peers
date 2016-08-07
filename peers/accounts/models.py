from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

import uuid
from random import choice
from string import lowercase

from .managers import ProfileManager


def user_image_upload(instance, filename):
    return "profile_images/user%s" % (filename)

ADMIN = "1"
USER = "2"

USER_ROLE_CHOICES = [
    (ADMIN, "Admin"),
    (USER, "User"),
]


class Profile(AbstractBaseUser, PermissionsMixin):
    """
    user model containing user's info
    as name/email/username/address
    """
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100, null=True, blank=True)
    email = models.EmailField(_("Email"), max_length=70, unique=True)
    username = models.CharField(_("Profilename"), max_length=32, unique=True)
    contact_no = models.CharField(_("Contact Number"), max_length=15, validators=[
        RegexValidator(r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'),
        MinLengthValidator(6),
        MaxLengthValidator(15)], blank=True, null=True)
    role = models.CharField(
        _("Profile Role"), max_length=1, choices=USER_ROLE_CHOICES, default=2)
    email_alerts = models.BooleanField(_("Email Alerts"), default=False)
    sms_alerts = models.BooleanField(_("SMS Alerts"), default=False)
    account_activated = models.BooleanField(_("Account Activated"), default=False)
    is_staff = models.BooleanField(
        _("Staff Status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."))

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_("Designates whether this user should be treated as "
                    "active. Unselect this instead of deleting accounts."))
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    uuid = models.UUIDField(_("Profile Unique ID"), default=uuid.uuid4, editable=False)
    created = models.DateTimeField(_("Created On"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated On"), auto_now=True)
    delete = models.BooleanField(_("Delete"), default=False)

    objects = ProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        app_label = "accounts"

    def __unicode__(self):
        return "%s" % (self.email)

    def save(self, *args, **kwargs):
        """
        ensure instance has usable password when created &
        add username by default when saving user
        """
        if self.pk is None:
            first_name = "_".join(str(self.first_name).split()).replace(".", "_")
            self.username = first_name.lower() + '_' + ''.join([choice(lowercase) for i in xrange(3)])
        if not self.pk and self.has_usable_password() is False:
            self.set_password(self.password)

        super(Profile, self).save(*args, **kwargs)

    def get_full_name(self):
        """
        return user's full name i.e. first_name and last_name
        """
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return "%s" % (self.first_name)
