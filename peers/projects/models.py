from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

import uuid

from .managers import (
    ProjectManager, CreditsAchievedManager, CreditsValueMappingManager, StrategyManager,
    StrategyQuestionManager, ProjectStrategyManager, ProjectElectricityPlantManager,
    ElectricityPlantUnitManager, ProjectPlantManager, ProjectPlantUnitManager, CreditsKeywordManager
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

    CITY = "city"
    CAMPUS = "campus"
    SUPPLY = "supply"

    PROJECT_TYPE_CHOICES = [
        (CITY, "City"),
        (CAMPUS, "Campus"),
        (SUPPLY, "Supply")
    ]

    name = models.CharField(_("Project Name"), max_length=120)
    region = models.CharField(_("Project Region"), max_length=200, blank=True, null=True)
    description = models.TextField(_("Project Description"))
    city = models.CharField(_("City"), max_length=40)
    state = models.CharField(_("State/Province"), max_length=40)
    country = models.CharField(_("Country"), max_length=40)
    zipcode = models.CharField(_("Zipcode"), max_length=20)
    project_type = models.CharField(_("Project Type"), max_length=10, choices=PROJECT_TYPE_CHOICES, blank=True, null=True)
    # project_subtype = models.CharField(_("Project SubType"), max_length=2, choices=PROJECT_SUBTYPE_CHOICES)
    org_name = models.CharField(_("Organization Name"), max_length=80)
    # org_address = models.TextField(_("organisation Address"))
    poc_name = models.CharField(_("Point Of Contact Name"), max_length=80)
    poc_contact = models.CharField(_("Contact Number"), max_length=15, validators=[
        RegexValidator(r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'),
        MinLengthValidator(6),
        MaxLengthValidator(15)], blank=True, null=True)
    poc_email = models.EmailField(_("Point of Contact Email"), max_length=80)
    poc_designation = models.CharField(_("Point of Contact Designation"), max_length=80)

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


class ProjectSpecificInfo(models.Model):
    """
    model to update project specific data
    """
    MEGA_WATT_HOURS = "MWh"
    MILLION_UNITS = "MUs"
    KILO_WATT_HOURS = "kWh"
    BRITISH_THERMAL_UNIT = "MmBTU"
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

    ITR_FRQ1 = "FRQ1"
    ITR_FRQ2 = "FRQ2"
    ITR_FRQ3 = "FRQ3"

    INTERRUPTION_FREQUENCY_RANGE = [
        (ITR_FRQ1, "O to < 15 mins"),
        (ITR_FRQ2, ">15 mins to 60 mins"),
        (ITR_FRQ3, "More than 60 mins")
    ]

    MGA = "mga"
    SCREENING = "scr"
    PPP = "ppp"

    PAYMENT_OPTION_CHOICES = [
        (MGA, "Micro Grid 8760 Analysis"),
        (SCREENING, "Screening"),
        (PPP, "PEER Participation Package")
    ]

    project = models.ForeignKey(Project, related_name=_("project_specific"))
    project_sei = models.DecimalField(_("Project SEI value"), max_digits=12, decimal_places=2, blank=True, null=True)
    project_score = models.IntegerField(_("Project Score"), blank=True, null=True)
    frequency_range = models.CharField(_("Interruption Frequency Range"), max_length=5, choices=INTERRUPTION_FREQUENCY_RANGE, blank=True, null=True)
    customer_served = models.DecimalField(_("Customer Served with Advance Meter"), max_digits=3, decimal_places=1, blank=True, null=True)
    res_customer = models.IntegerField(_("No of Residential Customer"), blank=True, null=True)
    comm_industrial1 = models.IntegerField(_("No of small commercial and industrial customers"), blank=True, null=True)
    comm_industrial2 = models.IntegerField(_("No of large commercial and industrial customers"), blank=True, null=True)
    electricity_unit = models.CharField(_("Electricity Default Unit"), max_length=10, blank=True, null=True)
    thermal_unit = models.CharField(_("Thermal/Heat Energy Unit"), max_length=15, blank=True, null=True)
    currency = models.CharField(_("Default Currency"), max_length=20, blank=True, null=True)
    annual_customer_load = models.DecimalField(_("Annual Customer Load"), max_digits=12, decimal_places=2, blank=True, null=True)
    customer_hr_peak_demand = models.DecimalField(_("Customer Annual Hourly Peak Demand"), max_digits=12, decimal_places=2, blank=True, null=True)
    peak_demand_unit = models.CharField(_("Peak Demand Unit"), max_length=10, default=MEGA_WATTS)
    annual_purchased_elec = models.DecimalField(_("Annual Purchased Electricity"), max_digits=12, decimal_places=2, blank=True, null=True)
    purchased_hr_peak_demand = models.DecimalField(_("Purchased annual hourly peak demand"), max_digits=12, decimal_places=2, blank=True, null=True)
    purchased_hr_unit = models.CharField(_("Purchased Peak Demand Unit"), max_length=10, default=MEGA_WATTS)
    tnd_losses = models.DecimalField(_("T&D Losses"), max_digits=5, decimal_places=2, blank=True, null=True)
    payment_option = models.CharField(_("Payment Option"), max_length=3, choices=PAYMENT_OPTION_CHOICES, blank=True, null=True)

    tot_local_elec_generation = models.DecimalField(_("Total Local Electricity Generation"), max_digits=12, decimal_places=2, blank=True, null=True)
    turbine_elec = models.DecimalField(_("Local Turbine Electricity Generation"), max_digits=12, decimal_places=2, blank=True, default=0)
    chp_elec = models.DecimalField(_("Local CHP natual gas Electricity Generation"), max_digits=12, decimal_places=2, blank=True, default=0)
    high_efficiency_gas_elec = models.DecimalField(_("Local High Efficiency Electricity generation"), max_digits=12, decimal_places=2, blank=True, default=0)
    local_other_gas_elec = models.DecimalField(_("Local other Gas Electricity Generation"), max_digits=12, decimal_places=2, blank=True, default=0)
    wind_solar_pv_elec = models.DecimalField(_("Wind Solar PV Electricity Generation"), max_digits=12, decimal_places=2, blank=True, default=0)
    biomass_elec = models.DecimalField(_("Biomass Electricity Generation"), max_digits=12, decimal_places=2, blank=True, default=0)
    geothermal_elec = models.DecimalField(_("Geothermal Electricity Generation"), max_digits=12, decimal_places=2, blank=True, default=0)
    other_local_elec = models.DecimalField(_("Other Renewable Electricity Generation"), max_digits=12, decimal_places=2, blank=True, default=0)

    tot_local_generation_capacity = models.DecimalField(_("Total Local Electricity Generation Capacity"), max_digits=12, decimal_places=2, blank=True, null=True)
    turbine_elec_capacity = models.DecimalField(_("Local Turbine Electricity Generation Capacity"), max_digits=12, decimal_places=2, blank=True, null=True)
    chp_elec_capacity = models.DecimalField(_("Local CHP natual gas Electricity Generation Capacity"), max_digits=12, decimal_places=2, blank=True, null=True)
    high_efficiency_gas_elec_capacity = models.DecimalField(_("Local High Efficiency Electricity generation Capacity"), max_digits=12, decimal_places=2, blank=True, null=True)
    local_other_gas_elec_capacity = models.DecimalField(_("Local other Gas Electricity Generation Capacity"), max_digits=12, decimal_places=2, blank=True, null=True)
    wind_solar_pv_elec_capacity = models.DecimalField(_("Wind Solar PV Electricity Generation Capacity"), max_digits=12, decimal_places=2, blank=True, null=True)
    biomass_elec_capacity = models.DecimalField(_("Biomass Electricity Generation Capacity"), max_digits=12, decimal_places=2, blank=True, null=True)
    geothermal_elec_capacity = models.DecimalField(_("Geothermal Electricity Generation Capacity"), max_digits=12, decimal_places=2, blank=True, null=True)
    other_local_elec_capacity = models.DecimalField(_("Other Renewable Electricity Generation Capacity"), max_digits=12, decimal_places=2, blank=True, null=True)

    bulk_coal = models.DecimalField(_("Purchased Bulk Coal Electricity"), max_digits=12, decimal_places=2, blank=True, default=0)
    bulk_petroleum = models.DecimalField(_("Purchased Bulk Petroleum Electricity"), max_digits=12, decimal_places=2, blank=True, default=0)
    bulk_simple_gas = models.DecimalField(_("Purchased Bulk Simple Gas Electricity"), max_digits=12, decimal_places=2, blank=True, default=0)
    bulk_high_eff_gas = models.DecimalField(_("Purchased Bulk High Efficiency Electricity"), max_digits=12, decimal_places=2, blank=True, default=0)
    bulk_hydro = models.DecimalField(_("Purchased Bulk Hydro Electricity"), max_digits=12, decimal_places=2, blank=True, default=0)
    bulk_nuclear = models.DecimalField(_("Purchased Bulk Nuclear Electricity"), max_digits=12, decimal_places=2, blank=True, default=0)
    bulk_solar_pv_wind = models.DecimalField(_("Purchased Bulk Solar and Wind Electricity"), max_digits=12, decimal_places=2, blank=True, default=0)

    class Meta:
        verbose_name = _("ProjectSpecificInfo")
        verbose_name_plural = _("ProjectSpecificInfos")
        app_label = "projects"

    def __unicode__(self):
        return "%s" % (self.project.name)


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

    DESIGN_CONSIDERATION = "DCN"
    PERFORMANCE_OUTCOME = "PO"
    DEMONSTRATED_CAPABILITY = "DC"
    PERFORMANCE_TRANSPARENCY = "PT"
    STANDARD_PROCESS = "SP"

    CREDIT_CRITERIA_CHOICES = [
        (DESIGN_CONSIDERATION, "Design Consideration"),
        (PERFORMANCE_OUTCOME, "Performance Outcome"),
        (DEMONSTRATED_CAPABILITY, "Demonstrated Capability"),
        (PERFORMANCE_TRANSPARENCY, "Performance Transparency"),
        (STANDARD_PROCESS, "Standard Process")
    ]

    PREREQUISTIC = "PR"
    CORE = "CO"
    BONUS = "BO"

    CREDIT_TYPE_CHOICES = [
        (PREREQUISTIC, "Pre Requistic"),
        (CORE, "Core"),
        (BONUS, "Bonus")
    ]

    # project = models.ForeignKey(Project, related_name=_("project_credit"))
    credit_name = models.CharField(_("Credit Name"), max_length=120)
    category = models.CharField(_("Credit Category"), max_length=5, choices=CREDIT_CATEGORY_CHOICES)
    city_credit = models.BooleanField(_("City Credit"), default=False)
    campus_credit = models.BooleanField(_("Campus Credit"), default=False)
    supply_credit = models.BooleanField(_("Supply Credit"), default=False)
    criteria = models.CharField(_("Credit Criteria"), max_length=5, choices=CREDIT_CRITERIA_CHOICES)
    type = models.CharField(_("Credit Type"), max_length=5, choices=CREDIT_TYPE_CHOICES)
    intent = models.TextField(_("Credit Intent"))
    delete = models.BooleanField(_("Delete"), default=False)

    objects = CreditsAchievedManager()

    class Meta:
        verbose_name = _("CreditsAchieved")
        verbose_name_plural = _("CreditsAchieveds")
        app_label = "projects"

    def __unicode__(self):
        return "%s" % (self.credit_name)


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
    AMR_1A = "amr1a"
    AMR_1B = "amr1b"
    SEI_EE = "seiee"
    LRG_EE = "lrgee"
    EEE_OE = "eeeoe"
    AMI_CC = "amicc"
    NTM_CC = "ntmcc"

    STRATEGY_UNIQUE_CHOICES = [
        (AMR_1A, "Advance Metering 1A"),
        (AMR_1B, "Advance Metering 1B"),
        (SEI_EE, "Source Energy Intensity EE"),
        (LRG_EE, "Local Renewable Generation EE"),
        (EEE_OE, "Electricity Energy Efficiency OE"),
        (AMI_CC, "Advance Metering Infrastructure CC"),
        (NTM_CC, "Net Metering CC")
    ]

    credit = models.ForeignKey(CreditsAchieved, related_name=_("credit_strategy"))
    unique_id = models.CharField(_("Strategy Unique ID"), max_length=5, choices=STRATEGY_UNIQUE_CHOICES)
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
        return "%s" % (self.name)


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
    EES_3_1 = "EES31"
    EES_3_2 = "EES32"
    EES_3_3 = "EES33"
    EES_3_4 = "EES34"
    EEC_3_5 = "EEC35"
    EES_12_1 = "EES121"
    EEC_12_2 = "EEC122"
    OES_6_1 = "OES61"
    OEC_6_2 = "OEC62"
    CCC_1_1 = "CCC11"
    CCC_1_2 = "CCC12"
    CCC_1_3 = "CCC13"
    CCC_1_4 = "CCC14"
    CCC_1_5 = "CCC15"
    CCC_1_6 = "CCC16"
    CCC_1_7 = "CCC17"
    CCS_1_1 = "CCS11"
    CCS_1_2 = "CCS12"
    CCS_1_3 = "CCS13"
    CCS_1_4 = "CCS14"
    CCS_1_5 = "CCS15"
    CCS_1_6 = "CCS16"
    CCS_1_7 = "CCS17"
    CCS_1_8 = "CCS18"

    QUESTION_CODE_CHOICES = [
        (RRS_1_1, "RRS-1.1"),
        (RRS_1_2, "RRS-1.2"),
        (RRS_1_3, "RRS-1.3"),
        (RRC_1_4, "RRC-1.4"),
        (RRC_1_5, "RRC-1.5"),
        (RRC_1_6, "RRC-1.6"),
        (RRS_1_7, "RRS-1.7"),
        (RRC_1_8, "RRC-1.8"),
        (EES_3_1, "EES-3.1"),
        (EES_3_2, "EES-3.2"),
        (EES_3_3, "EES-3.3"),
        (EES_3_4, "EES-3.4"),
        (EEC_3_5, "EEC-3.5"),
        (EES_12_1, "EES-12.1"),
        (EEC_12_2, "EEC-12.2"),
        (OES_6_1, "OES-6.1"),
        (OEC_6_2, "OEC-6.2"),
        (CCC_1_1, "CCC-1.1"),
        (CCC_1_2, "CCC-1.2"),
        (CCC_1_3, "CCC-1.3"),
        (CCC_1_4, "CCC-1.4"),
        (CCC_1_5, "CCC-1.5"),
        (CCC_1_6, "CCC-1.6"),
        (CCC_1_7, "CCC-1.7"),
        (CCS_1_1, "CCS-1.1"),
        (CCS_1_2, "CCS-1.2"),
        (CCS_1_3, "CCS-1.3"),
        (CCS_1_4, "CCS-1.4"),
        (CCS_1_5, "CCS-1.5"),
        (CCS_1_6, "CCS-1.6"),
        (CCS_1_7, "CCS-1.7"),
        (CCS_1_8, "CCS-1.8"),
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

    ITR_FRQ1 = "1"
    ITR_FRQ2 = "2"
    ITR_FRQ3 = "3"

    INTERRUPTION_FREQUENCY_RANGE = [
        (ITR_FRQ1, "O to < 15 mins"),
        (ITR_FRQ2, ">15 mins to 60 mins"),
        (ITR_FRQ3, "More than 60 mins")
    ]

    strategy = models.ForeignKey(Strategy, related_name=_("strategy_question"))
    question = models.TextField(_("Question"))
    code = models.CharField(_("Question Code"), max_length=10, choices=QUESTION_CODE_CHOICES)
    qtype = models.CharField(_("Question Type"), max_length=10, choices=QUESTION_TYPE_CHOICES)

    objects = StrategyQuestionManager()

    class Meta:
        verbose_name = _("StrategyQuestion")
        verbose_name_plural = _("StrategyQuestions")
        app_label = "projects"

    def __unicode__(self):
        return "%s" % (self.code)


def question_file_upload(instance, filename):
    return "strategy/docs%s" % (filename)


class ProjectStrategy(models.Model):
    """
    mapping of project with question
    """
    project = models.ForeignKey(Project, related_name=_("project_question"))
    strategy = models.ForeignKey(Strategy, related_name=_("project_strategy"))
    file = models.FileField(_("Question File for Project"), upload_to=question_file_upload, blank=True, null=True)
    status = models.CharField(_("Strategy Status"), max_length=20, default="completed")
    submitted_by = models.ForeignKey(Profile, related_name=_("question_answered_user"))

    objects = ProjectStrategyManager()

    class Meta:
        verbose_name = _("ProjectStrategy")
        verbose_name_plural = _("ProjectStrategys")
        app_label = "projects"

    def __unicode__(self):
        return "%s" % (self.project.name)


class ElectricityPlant(models.Model):
    """
    Plantwise SEI for the specified country
    """
    COAL = "coal"
    NUCLEAR = "nuclear"
    GAS = "cas"
    PETROLEUM = "Petroleum"
    SIMPLE_GAS = "simple gas"
    WIND = "wind"
    (PETROLEUM, "Petroleum"),
    (SIMPLE_GAS, "Simple Gas"),
    (WIND, "Wind"),
    OTHER_MEAN = "other mean"

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

    plant_name = models.CharField(_("Plant Name"), max_length=50, blank=True, null=True)
    fuel_type = models.CharField(_("Fuel Type"), max_length=20, choices=FUEL_TYPE_CHOICES, default=OTHER_MEAN)
    sei_value = models.CharField(_("SEI Value"), max_length=10, default=0)
    utility = models.CharField(_("Plant Utility"), max_length=10, choices=PLANT_UTILITY_CHOICES)
    type = models.CharField(_("Plant Type"), max_length=10, choices=PLANT_TYPE_CHOICES)
    state = models.CharField(_("Plant State"), max_length=30)
    country = models.CharField(_("Plant Country"), max_length=30)
    delete = models.BooleanField(_("Delete"), default=False)

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
        return "%s:%s" % (self.plant.plant_name) % str(self.unit_no)


class ProjectPlant(models.Model):
    """
    Plantwise SEI for the specified country
    """
    COAL = "coal"
    NUCLEAR = "nuclear"
    GAS = "gas"
    PETROLEUM = "petroleum"
    SIMPLE_GAS = "simple-gas"
    WIND = "wind"
    OTHER_MEAN = "other-mean"

    FUEL_TYPE_CHOICES = [
        (COAL, "Coal"),
        (NUCLEAR, "Nuclear"),
        (GAS, "Gas"),
        (PETROLEUM, "Petroleum"),
        (SIMPLE_GAS, "Simple Gas"),
        (WIND, "Wind"),
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

    LOCAL = "local"
    BULK = "bulk"

    GENERATION_TYPE_CHOICES = [
        (LOCAL, "Local"),
        (BULK, "Bulk")
    ]

    project = models.ForeignKey(Project, related_name=_("project_plant"))
    plant_name = models.CharField(_("Plant Name"), max_length=50, blank=True, null=True)
    fuel_type = models.CharField(_("Fuel Type"), max_length=20, choices=FUEL_TYPE_CHOICES, default=OTHER_MEAN)
    sei_value = models.DecimalField(_("SEI Value"), max_digits=10, decimal_places=2, default=0)
    utility = models.CharField(_("Plant Utility"), max_length=10, choices=PLANT_UTILITY_CHOICES)
    type = models.CharField(_("Plant Type"), max_length=10, blank=True, null=True, choices=PLANT_TYPE_CHOICES)
    state = models.CharField(_("Plant State"), max_length=30)
    country = models.CharField(_("Plant Country"), max_length=30)
    electricity_delivered = models.CharField(_("Electricity Delivered to Project"), max_length=10, default=0)
    generation_type = models.CharField(_("Type of Generation"), max_length=10, choices=GENERATION_TYPE_CHOICES)
    thermal_energy = models.CharField(_("Recovered Thermal Energy"), max_length=15)
    delete = models.BooleanField(_("Delete"), default=False)

    objects = ProjectPlantManager()

    class Meta:
        verbose_name = _("ProjectPlant")
        verbose_name_plural = _("ProjectPlants")
        app_label = "projects"

    def __unicode__(self):
        return "%s" % (self.plant_name)


class ProjectPlantUnit(models.Model):
    """
    electricity plant's unit capacity and date
    """
    plant = models.ForeignKey(ProjectPlant, related_name=_("project_plant_unit"))
    unit_no = models.IntegerField(_("Plant Unit No."))
    capacity = models.CharField(_("Plant Unit capacity"), max_length=10)
    commissioning = models.DateTimeField(_("Plant Commissioning Date"), blank=True, null=True)

    objects = ProjectPlantUnitManager()

    class Meta:
        verbose_name = _("ProjectPlantUnit")
        verbose_name_plural = _("ProjectPlantUnits")
        app_label = "projects"

    def __unicode__(self):
        return "%s:%s" % (self.plant.plant_name) % str(self.unit_no)


class CreditsKeyword(models.Model):
    """
    model to map credits with keyword
    """
    credit = models.ForeignKey(CreditsAchieved, related_name=_("credit_keyword"))
    keyword = models.CharField(_("keyword"), max_length=100)
    description = models.TextField(_("Keyword Description"), blank=True, null=True)

    objects = CreditsKeywordManager()

    class Meta:
        verbose_name = _("CreditsKeyword")
        verbose_name_plural = _("CreditsKeywords")
        app_label = "projects"

    def __unicode__(self):
        return "%s" % (self.keyword)
