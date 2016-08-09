from django.contrib import admin

from .models import (
    Project, CreditsAchieved, CreditsValueMapping, Strategy, StrategyQuestion, ProjectQuestion,
    ElectricityPlant, ElectricityPlantUnit, ProjectPlantMapping, CreditsKeyword)

models = [
    Project, CreditsAchieved, CreditsValueMapping, Strategy, StrategyQuestion, ProjectQuestion,
    ElectricityPlant, ElectricityPlantUnit, ProjectPlantMapping, CreditsKeyword]

admin.site.register(models)
