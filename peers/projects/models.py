from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

import uuid

from .managers import ProjectManager
from accounts.models import Profile


BASIC = "1"
SCREENING = "2"

PROJECT_STATUS_CHOICES = [
    (BASIC, "Basic"),
    (SCREENING, "Screening")
]


class Project(models.Model):
    """
    model to store project details
    """
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

    name = models.CharField(_("Project Name"), max_length=120)
    description = models.TextField(_("Project Description"))
    city = models.CharField(_("City"), max_length=40)
    state = models.CharField(_("State/Province"), max_length=40)
    country = models.CharField(_("Country"), max_length=40)
    project_type = models.CharField(_("Project Type"), max_length=1, choices=PROJECT_TYPE_CHOICES)
    project_subtype = models.CharField(_("Project SubType"), max_length=2, choices=PROJECT_SUBTYPE_CHOICES)
    org_name = models.CharField(_("Organization Name"), max_length=80)
    org_address = models.TextField(_("organisation Address"))
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
        return "%S" % (self.name)
