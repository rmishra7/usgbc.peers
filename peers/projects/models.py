from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

import uuid

from .managers import (
    ProjectManager, CreditsAchievedManager, CreditsValueMappingManager, StrategyManager,
    StrategyQuestionManager, ProjectQuestionManager, ProjectElectricityPlantManager,
    ElectricityPlantUnitManager, ProjectPlantMappingManager
    )
from accounts.models import Profile


class Project(models.Model):
    """
    model to store project details
    """
    BASIC = "1"
    SCREENING = "2"

    PROJECT_STATUS_CHOICES = [
        (BASIC, "Basic"),
        (SCREENING, "Screening")
    ]

    CITY = "1"
    CAMPUS = "2"
    SUPPLY = "3"

    PROJECT_TYPE_CHOICES = [
        (CITY, "City"),
        (CAMPUS, "Campus"),
        (SUPPLY, "Supply")
    ]

    MUNICIPAL_UTILITY = "1"
    SPECIAL_DISTRICT = "2"
    CITYWIDE = "3"
    INVESTOR_OWNED = "4"
    UNIVERSITY_CAMPUS = "5"
    INDUSTRIAL_PARK = "6"
    MILITARY_BASE = "7"
    LARGE_BUILDING = "8"
    CHP_POWER_PLANT = "9"
    INDUSTRIAL_FACILITY = "10"
    THIRD_PARTY_SUPPLIER = "11"
    OTHER = "12"

    PROJECT_SUBTYPE_CHOICES = [
        (MUNICIPAL_UTILITY, "Municipal Utility"),
        (SPECIAL_DISTRICT, "Special District"),
        (CITYWIDE, "City Wide"),
        (INVESTOR_OWNED, "Investor Owned"),
        (UNIVERSITY_CAMPUS, "University campus"),
        (INDUSTRIAL_PARK, "Industrial Park"),
        (MILITARY_BASE, "Military Base"),
        (LARGE_BUILDING, "Large Building"),
        (CHP_POWER_PLANT, "CHP Power Plant"),
        (INDUSTRIAL_FACILITY, "Industrial Facility"),
        (THIRD_PARTY_SUPPLIER, "Third Party Supplier"),
        (OTHER, "Other")
    ]

    MEGA_WATT_HOURS = "MWh"
    MILLION_UNITS = "MUs"
    KILO_WATT_HOURS = "kWh"
    BRITISH_THERMAL_UNIT = "BTU"
    CALORIES = "cal"
    JOULES = "joules"
    MEGA_WATTS = "MW"

    UNIT_CHOICES = [
        (MEGA_WATT_HOURS, "Mega watt-hours (MWh)"),
        (MILLION_UNITS, "Million units"),
        (KILO_WATT_HOURS, "Kilo watt-hours (kWh)"),
        (BRITISH_THERMAL_UNIT, "British thermal unit"),
        (CALORIES, "Calories"),
        (JOULES, "Joules"),
        (MEGA_WATTS, "Mega watt (MW)")
    ]

    name = models.CharField(_("Project Name"), max_length=120)
    description = models.TextField(_("Project Description"))
    city = models.CharField(_("City"), max_length=40)
    state = models.CharField(_("State/Province"), max_length=40)
    country = models.CharField(_("Country"), max_length=40)
    zipcode = models.CharField(_("Zipcode"), max_length=20)
    project_type = models.CharField(_("Project Type"), max_length=1, choices=PROJECT_TYPE_CHOICES, blank=True, null=True)
    # project_subtype = models.CharField(_("Project SubType"), max_length=2, choices=PROJECT_SUBTYPE_CHOICES)
    org_name = models.CharField(_("Organization Name"), max_length=80)
    org_address = models.TextField(_("organisation Address"))
    poc_name = models.CharField(_("Point Of Contact Name"), max_length=80)
    poc_contact = models.CharField(_("Contact Number"), max_length=15, validators=[
        RegexValidator(r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'),
        MinLengthValidator(6),
        MaxLengthValidator(15)], blank=True, null=True)
    poc_email = models.EmailField(_("Point of Contact Email"), max_length=80)
    poc_designation = models.CharField(_("Point of Contact Designation"), max_length=80)
    res_customer = models.IntegerField(_("No of Residential Customer"), blank=True, null=True)
    comm_industrial1 = models.IntegerField(_("No of small commercial and industrial customers"), blank=True, null=True)
    comm_industrial2 = models.IntegerField(_("No of large commercial and industrial customers"), blank=True, null=True)
    annual_customer_load = models.CharField(_("Annual Customer Load"), max_length=20, blank=True, null=True)
    customer_hr_peak_demand = models.CharField(_("Customer Annual Hourly Peak Demand"), max_length=20, blank=True, null=True)
    peak_demand_unit = models.CharField(_("Peak Demand Unit"), max_length=10, default=MEGA_WATTS)
    annual_purchased_elec = models.CharField(_("Annual Purchased Electricity"), max_length=20, blank=True, null=True)
    purchased_hr_peak_demand = models.CharField(_("Purchased annual hourly peak demand"), max_length=10, blank=True, null=True)
    purchased_hr_unit = models.CharField(_("Purchased Peak Demand Unit"), max_length=10, default=MEGA_WATTS)
    tnd_losses = models.CharField(_("T&D Losses"), max_length=10, blank=True, null=True)
    tot_local_elec_generation = models.CharField(_("Total Local Electricity Generation"), max_length=10, blank=True, null=True)
    turbine_elec = models.CharField(_("Local Turbine Electricity Generation"), max_length=10, blank=True, null=True)
    chp_elec = models.CharField(_("Local CHP natual gas Electricity Generation"), max_length=10, blank=True, null=True)
    high_efficiency_gas_elec = models.CharField(_("Local High Efficiency Electricity generation"), max_length=10, blank=True, null=True)
    local_other_gas_elec = models.CharField(_("Local other Gas Electricity Generation"), max_length=10, blank=True, null=True)
    wind_solar_pv_elec = models.CharField(_("Wind Solar PV Electricity Generation"), max_length=10, blank=True, null=True)
    biomass_elec = models.CharField(_("Biomass Electricity Generation"), max_length=10, blank=True, null=True)
    geothermal_elec = models.CharField(_("Geothermal Electricity Generation"), max_length=10, blank=True, null=True)
    other_local_elec = models.CharField(_("Other Renewable Electricity Generation"), max_length=10, blank=True, null=True)
    status = models.CharField(_("Project Status"), max_length=1, choices=PROJECT_STATUS_CHOICES)
    uuid = models.UUIDField(_("Project Unique ID"), default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Profile, related_name=_("project_owner"))
    created_by = models.ForeignKey(Profile, related_name=_("project_create_by"))
    updated_by = models.ForeignKey(Profile, related_name=_("project_updated_by"))
    destroyed_by = models.ForeignKey(Profile, related_name=_("project_destroyed_by"), null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    delete = models.BooleanField(_("Delete"), default=False)

    objects = ProjectManager()

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        app_label = "projects"

    def __unicode__(self):
        return "%s" % (self.name)


class CreditsAchieved(models.Model):
    """
    credits achieved for the project
    """
    ENERGY_EFF_ENV = "EEE"
    RELIABILITY_RESILIENCY = "RR"
    OPERATION_EFFECTIVE = "OE"
    CUSTOMER_CONTRIBUTION = "CC"

    CREDIT_CATEGORY_CHOICES = [
        (ENERGY_EFF_ENV, "Energy Efficiency & Environment"),
        (RELIABILITY_RESILIENCY, "Reliability Resiliency"),
        (OPERATION_EFFECTIVE, "Operation Effectiveness"),
        (CUSTOMER_CONTRIBUTION, "Customer Contribution")
    ]

    DCN = "DCN"
    PO = "PO"
    DC = "DC"
    PT = "PT"
    SP = "SP"

    CREDIT_CRITERIA_CHOICES = [
        (DCN, "DCN"),
        (PO, "PO"),
        (DC, "DC"),
        (PT, "PT"),
        (SP, "SP")
    ]

    PR = "PR"
    CO = "CO"
    BO = "BO"
    PR = "PR"

    CREDIT_TYPE_CHOICES = [
        (PR, "PR"),
        (CO, "CO"),
        (BO, "BO"),
        (PR, "PR")
    ]

    # project = models.ForeignKey(Project, related_name=_("project_credit"))
    credit_name = models.CharField(_("Credit Name"), max_length=120)
    category = models.CharField(_("Credit Category"), max_length=1, choices=CREDIT_CATEGORY_CHOICES)
    city_credit = models.BooleanField(_("City Credit"), default=False)
    campus_credit = models.BooleanField(_("Campus Credit"), default=False)
    supply_credit = models.BooleanField(_("Supply Credit"), default=False)
    criteria = models.CharField(_("Credit Criteria"), max_length=2, choices=CREDIT_CRITERIA_CHOICES)
    type = models.CharField(_("Credit Type"), max_length=2, choices=CREDIT_TYPE_CHOICES)
    intent = models.CharField(_("Credit Intent"), max_length=200)
    delete = models.BooleanField(_("Delete"), default=False)

    objects = CreditsAchievedManager()

    class Meta:
        verbose_name = _("CreditsAchieved")
        verbose_name_plural = _("CreditsAchieveds")
        app_label = "projects"

    def __unicode__(self):
        return "%s:%s" % (self.project.name) % (self.credit_name)


class CreditsValueMapping(models.Model):
    """
    mapping of credits for calculated values like sei
    """
    from_credit = models.ForeignKey(CreditsAchieved, related_name=_("from_credit_obj"))
    to_credit = models.ForeignKey(CreditsAchieved, related_name=_("to_credit_obj"))
    value = models.CharField(_("Input Value"), max_length=10, default=0)

    objects = CreditsValueMappingManager()

    class Meta:
        verbose_name = _("CreditsValueMapping")
        verbose_name_plural = _("CreditsValueMappings")
        app_label = "projects"

    def __unicode__(self):
        return "%s" % (self.to_credit.credit_name)


class Strategy(models.Model):
    """
    strategy model for credits
    """
    credit = models.ForeignKey(CreditsAchieved, related_name=_("credit_strategy"))
    name = models.CharField(_("Strategy Name"), max_length=100)
    description = models.TextField(_("Strategy Description"), blank=True, null=True)
    successmessage = models.TextField(_("Strategy Success Message"), blank=True, null=True)
    failuremessage = models.TextField(_("Strategy Failure Message"), blank=True, null=True)
    required = models.BooleanField(_("Strategy Required"), default=False)
    delete = models.BooleanField(_("Delete"), default=False)

    objects = StrategyManager()

    class Meta:
        verbose_name = _("Strategy")
        verbose_name_plural = _("Strategys")
        app_label = "projects"

    def __unicode__(self):
        return "%s:%s" % (self.name)


class StrategyQuestion(models.Model):
    """
    question belongs with strategy
    """
    RRS_1_1 = "RRS11"
    RRS_1_2 = "RRS12"
    RRS_1_3 = "RRS13"
    RRC_1_4 = "RRC14"
    RRC_1_5 = "RRC15"
    RRC_1_6 = "RRC16"
    RRS_1_7 = "RRS17"
    RRC_1_8 = "RRC18"

    QUESTION_CODE_CHOICES = [
        (RRS_1_1, "RRS-1.1"),
        (RRS_1_2, "RRS-1.2"),
        (RRS_1_3, "RRS-1.3"),
        (RRC_1_4, "RRC-1.4"),
        (RRC_1_5, "RRC-1.5"),
        (RRC_1_6, "RRC-1.6"),
        (RRS_1_7, "RRS-1.7"),
        (RRC_1_8, "RRC-1.8")
    ]

    LABEL = "label"
    TEXT = "text"
    NARRATIVE = "narrative"
    YESNO = "yesno"
    CHECKBOX = "checkbox"
    RADIO = "radio"
    SELECT = "select"
    SLIDER = "slider"
    FILE = "file"

    QUESTION_TYPE_CHOICES = [
        (LABEL, 'Label'),
        (TEXT, 'Input Box'),
        (NARRATIVE, 'Narrative'),
        (YESNO, 'Yes/No'),
        (CHECKBOX, 'Checkbox'),
        (RADIO, 'Radio'),
        (SELECT, 'Dropdown'),
        (SLIDER, 'Slider'),
        (FILE, 'File Upload')
    ]

    strategy = models.ForeignKey(Strategy, related_name=_("strategy_question"))
    question = models.TextField(_("Question"))
    code = models.CharField(_("Question Code"), max_length=2, choices=QUESTION_CODE_CHOICES)
    qtype = models.CharField(_("Question Type"), max_length=1, choices=QUESTION_TYPE_CHOICES)

    objects = StrategyQuestionManager()

    class Meta:
        verbose_name = _("StrategyQuestion")
        verbose_name_plural = _("StrategyQuestions")
        app_label = "projects"

    def __unicode__(self):
        return "%s" % (self.code)


def question_file_upload(instance, filename):
    return "strategy/docs%s" % (filename)


class ProjectQuestion(models.Model):
    """
    mapping of project with question
    """
    project = models.ForeignKey(Project, related_name=_("project_question"))
    question = models.ForeignKey(StrategyQuestion, related_name=_("question_object"))
    output = models.CharField(_("Question output for project"), max_length=50)
    file = models.FileField(_("Question File for Project"), upload_to=question_file_upload, blank=True, null=True)

    objects = ProjectQuestionManager()

    class Meta:
        verbose_name = _("ProjectQuestion")
        verbose_name_plural = _("ProjectQuestions")
        app_label = "projects"

    def __unicode__(self):
        return "%s" % (self.project.name)


class ElectricityPlant(models.Model):
    """
    Plantwise SEI for the specified country
    """
    COAL = "Coal"
    NUCLEAR = "Nuclear"
    GAS = "Gas"
    OTHER_MEAN = "Other"

    FUEL_TYPE_CHOICES = [
        (COAL, "Coal"),
        (NUCLEAR, "Nuclear"),
        (GAS, "Gas"),
        (OTHER_MEAN, "Other")
    ]

    NTPC = "NTPC"
    NHPC = "NHPC"
    NPCIL = "NPCIL"
    IPGPCL = "IPGPCL"
    SEI = "SEI"

    PLANT_UTILITY_CHOICES = [
        (NTPC, "NTPC"),
        (NHPC, "NHPC"),
        (NPCIL, "NPCIL"),
        (IPGPCL, "IPGPCL"),
        (SEI, "SEI Solar Energy Pvt. Ltd.")
    ]

    THERMAL = "TRL"
    HYDRO = "HDR"
    PV = "PV"

    PLANT_TYPE_CHOICES = [
        (THERMAL, "Thermal"),
        (HYDRO, "Hydro"),
        (PV, "PV")
    ]

    plant_name = models.CharField(_("Plant Name"), max_length=50)
    fuel_type = models.CharField(_("Fuel Type"), max_length=1, choices=FUEL_TYPE_CHOICES, blank=True, null=True)
    sei_value = models.CharField(_("SEI Value"), max_length=10, default=0)
    utility = models.CharField(_("Plant Utility"), max_length=1, choices=PLANT_UTILITY_CHOICES)
    type = models.CharField(_("Plant Type"), max_length=1, choices=PLANT_TYPE_CHOICES)
    state = models.CharField(_("Plant State"), max_length=30)
    country = models.CharField(_("Plant Country"), max_length=30)
    delete = models.BooleanField(_("Delete"), default=True)

    objects = ProjectElectricityPlantManager()

    class Meta:
        verbose_name = _("ElectricityPlant")
        verbose_name_plural = _("ElectricityPlants")
        app_label = "projects"

    def __unicode__(self):
        return "%s" % (self.plant_name)


class ElectricityPlantUnit(models.Model):
    """
    electricity plant's unit capacity and date
    """
    plant = models.ForeignKey(ElectricityPlant, related_name=_("plant_unit"))
    unit_no = models.IntegerField(_("Plant Unit No."))
    capacity = models.CharField(_("Plant Unit capacity"), max_length=10)
    commissioning = models.DateTimeField(_("Plant Commissioning Date"), blank=True, null=True)

    objects = ElectricityPlantUnitManager()

    class Meta:
        verbose_name = _("ElectricityPlantUnit")
        verbose_name_plural = _("ElectricityPlantUnits")
        app_label = "projects"

    def __unicode__(self):
        return "%s:%s" % (self.plant_name) % str(self.unit_no)


class ProjectPlantMapping(models.Model):
    """
    mapping of project with plant from which it getting Electricity
    """
    project = models.ForeignKey(Project, related_name=_("project_plant"))
    plant = models.ForeignKey(ElectricityPlant, related_name=_("elec_plant"))
    electricity_deliver = models.CharField(_("Electricity Delivered to Project"), max_length=10, default=0)

    objects = ProjectPlantMappingManager()

    class Meta:
        verbose_name = _("ProjectPlantMapping")
        verbose_name_plural = _("ProjectPlantMappings")
        app_label = "projects"

    def __unicode__(self):
        return "%s" % (self.project.name)
