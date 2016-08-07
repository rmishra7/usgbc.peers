
from django.db.models.query import QuerySet
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

from .mixins import ProfileMixin


class ProfileQuerySet(QuerySet, ProfileMixin):
    pass


class ProfileManager(BaseUserManager):
    """
    a custom user manager used for custom user model to support in create user
    without username(just email)
    """
    def _create_user(self, email, password, is_staff, is_superuser, **kwargs):
        if not email:
            raise ValueError('email must be provided.')
        email = self.normalize_email(email).lower()
        user = self.model(
            email=email, is_staff=is_staff, is_superuser=is_superuser,
            is_active=True, date_joined=timezone.now(), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self):
        return ProfileQuerySet(self.model, using=self._db).filter(delete=False)

    def create_user(self, email, password=None, **kwargs):
        return self._create_user(email, password, False, False, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        return self._create_user(email, password, True, True, **kwargs)
