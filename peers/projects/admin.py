from django.contrib import admin

from .models import (
    Project, ProjectSpecificInfo, CreditsAchieved, CreditsValueMapping, Strategy,
    StrategyQuestion, ProjectStrategy, ElectricityPlant, ElectricityPlantUnit,
    ProjectPlant, ProjectPlantUnit, CreditsKeyword
    )

models = [
    Project, ProjectSpecificInfo, CreditsAchieved, CreditsValueMapping, Strategy,
    StrategyQuestion, ProjectStrategy, ElectricityPlant, ElectricityPlantUnit,
    ProjectPlant, ProjectPlantUnit, CreditsKeyword]

admin.site.register(models)
