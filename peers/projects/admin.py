from django.contrib import admin

from .models import (
    Project, CreditsAchieved, CreditsValueMapping, Strategy, StrategyQuestion, ProjectStrategy,
    ElectricityPlant, ElectricityPlantUnit, ProjectPlant, ProjectPlantUnit, CreditsKeyword,
    ProjectSpecificInfo)

models = [
    Project, CreditsAchieved, CreditsValueMapping, Strategy, StrategyQuestion, ProjectStrategy,
    ElectricityPlant, ElectricityPlantUnit, ProjectPlant, ProjectPlantUnit, CreditsKeyword,
    ProjectSpecificInfo]

admin.site.register(models)
