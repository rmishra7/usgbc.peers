
from django.db.models.query import QuerySet
from django.db import models

from .mixins import (
    ProjectMixin, CreditsAchievedMixin, StrategyMixin, ProjectQuestionMixin, StrategyQuestionMixin,
    CreditsValueMappingMixin, ProjectPlantMappingMixin, ElectricityPlantUnitMixin,
    ProjectElectricityPlantMixin
    )


class ProjectQuerySet(QuerySet, ProjectMixin):
    pass


class ProjectManager(models.Manager, ProjectMixin):

    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db).filter(delete=False)


class CreditsAchievedQuerySet(models.Manager, CreditsAchievedMixin):
    pass


class CreditsAchievedManager(models.Manager, CreditsAchievedMixin):

    def get_queryset(self):
        return CreditsAchievedQuerySet(self.model, using=self._db).filter(delete=False)


class CreditsValueMappingQuerySet(models.Manager, CreditsValueMappingMixin):
    pass


class CreditsValueMappingManager(models.Manager, CreditsValueMappingMixin):

    def get_queryset(self):
        return CreditsValueMappingQuerySet(self.model, using=self._db).filter(delete=False)


class StrategyQuerySet(models.Manager, StrategyMixin):
    pass


class StrategyManager(models.Manager, StrategyMixin):

    def get_queryset(self):
        return StrategyQuerySet(self.model, using=self._db).filter(delete=False)


class StrategyQuestionQuerySet(models.Manager, StrategyQuestionMixin):
    pass


class StrategyQuestionManager(models.Manager, StrategyQuestionMixin):

    def get_queryset(self):
        return StrategyQuestionQuerySet(self.model, using=self._db).filter(delete=False)


class ProjectQuestionQuerySet(models.Manager, ProjectQuestionMixin):
    pass


class ProjectQuestionManager(models.Manager, ProjectQuestionMixin):

    def get_queryset(self):
        return ProjectQuestionQuerySet(self.model, using=self._db).filter(delete=False)


class ProjectElectricityPlantQuerySet(models.Manager, ProjectElectricityPlantMixin):
    pass


class ProjectElectricityPlantManager(models.Manager, ProjectElectricityPlantMixin):

    def get_queryset(self):
        return ProjectElectricityPlantQuerySet(self.model, using=self._db).filter(delete=False)


class ElectricityPlantUnitQuerySet(models.Manager, ElectricityPlantUnitMixin):
    pass


class ElectricityPlantUnitManager(models.Manager, ElectricityPlantUnitMixin):

    def get_queryset(self):
        return ElectricityPlantUnitQuerySet(self.model, using=self._db).filter(delete=False)


class ProjectPlantMappingQuerySet(models.Manager, ProjectPlantMappingMixin):
    pass


class ProjectPlantMappingManager(models.Manager, ProjectPlantMappingMixin):

    def get_queryset(self):
        return ProjectPlantMappingQuerySet(self.model, using=self._db).filter(delete=False)
