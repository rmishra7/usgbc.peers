
from django.db.models.query import QuerySet
from django.db import models

from .mixins import ProjectMixin


class ProjectQuerySet(QuerySet, ProjectMixin):
    pass


class ProjectManager(models.Manager, ProjectMixin):

    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db).filter(delete=False)
