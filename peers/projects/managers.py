
from django.db.models.query import QuerySet
from django.db import models

from .mixins import (
    ProjectMixin, CreditsAchievedMixin, StrategyMixin, ProjectQuestionMixin, StrategyQuestionMixin,
    CreditsValueMappingMixin, ProjectPlantMappingMixin, ElectricityPlantUnitMixin,
    ProjectElectricityPlantMixin, CreditsKeywordMixin
    )


class ProjectQuerySet(QuerySet, ProjectMixin):
    pass


class ProjectManager(models.Manager, ProjectMixin):

    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db)


class CreditsAchievedQuerySet(QuerySet, CreditsAchievedMixin):
    pass


class CreditsAchievedManager(models.Manager, CreditsAchievedMixin):

    def get_queryset(self):
        return CreditsAchievedQuerySet(self.model, using=self._db)


class CreditsValueMappingQuerySet(QuerySet, CreditsValueMappingMixin):
    pass


class CreditsValueMappingManager(models.Manager, CreditsValueMappingMixin):

    def get_queryset(self):
        return CreditsValueMappingQuerySet(self.model, using=self._db)


class StrategyQuerySet(QuerySet, StrategyMixin):
    pass


class StrategyManager(models.Manager, StrategyMixin):

    def get_queryset(self):
        return StrategyQuerySet(self.model, using=self._db)


class StrategyQuestionQuerySet(QuerySet, StrategyQuestionMixin):
    pass


class StrategyQuestionManager(models.Manager, StrategyQuestionMixin):

    def get_queryset(self):
        return StrategyQuestionQuerySet(self.model, using=self._db)


class ProjectQuestionQuerySet(QuerySet, ProjectQuestionMixin):
    pass


class ProjectQuestionManager(models.Manager, ProjectQuestionMixin):

    def get_queryset(self):
        return ProjectQuestionQuerySet(self.model, using=self._db)


class ProjectElectricityPlantQuerySet(QuerySet, ProjectElectricityPlantMixin):
    pass


class ProjectElectricityPlantManager(models.Manager, ProjectElectricityPlantMixin):

    def get_queryset(self):
        return ProjectElectricityPlantQuerySet(self.model, using=self._db)


class ElectricityPlantUnitQuerySet(QuerySet, ElectricityPlantUnitMixin):
    pass


class ElectricityPlantUnitManager(models.Manager, ElectricityPlantUnitMixin):

    def get_queryset(self):
        return ElectricityPlantUnitQuerySet(self.model, using=self._db)


class ProjectPlantMappingQuerySet(QuerySet, ProjectPlantMappingMixin):
    pass


class ProjectPlantMappingManager(models.Manager, ProjectPlantMappingMixin):

    def get_queryset(self):
        return ProjectPlantMappingQuerySet(self.model, using=self._db)


class CreditsKeywordQuerySet(QuerySet, CreditsKeywordMixin):
    pass


class CreditsKeywordManager(models.Manager, CreditsKeywordMixin):

    def get_queryset(self):
        return CreditsKeywordQuerySet(self.model, using=self._db)
