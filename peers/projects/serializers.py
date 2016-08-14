
from django.shortcuts import get_object_or_404

from rest_framework import serializers

from .models import (
    Project, ProjectQuestion, StrategyQuestion, CreditsAchieved, Strategy,
    ProjectSpecificInfo)
from accounts.serializers import ProfileMiniSerializer


class ProjectMiniSerializer(serializers.ModelSerializer):
    """
    ProjectMiniSerializer
    """
    class Meta:
        model = Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    project list/create serializer
    """
    project_owner = ProfileMiniSerializer(source='owner', read_only=True)
    created_by = ProfileMiniSerializer(read_only=True)
    updated_by = ProfileMiniSerializer(read_only=True)
    project_status = serializers.SerializerMethodField('get_project_status_detail')

    def get_project_status_detail(self, obj):
        return [item[1] for item in Project.PROJECT_STATUS_CHOICES if item[0] == obj.status][0]

    def validate(self, attrs):
        view = self.context.get('view')
        attrs['status'] = Project.BASIC
        attrs['owner'] = view.request.user
        attrs['created_by'] = view.request.user
        attrs['updated_by'] = view.request.user
        return attrs

    class Meta:
        model = Project
        fields = (
            'id', 'name', 'description', 'city', 'state', 'country', 'org_name',
            'poc_name', 'poc_contact', 'poc_email', 'poc_designation', 'created_by', 'project_type',
            'updated_by', 'created_at', 'uuid', 'updated_at', 'project_owner', 'project_status', 'zipcode')
        read_only_fields = ('uuid', )


class ProjectDetailSerializer(serializers.ModelSerializer):
    """
    project list/create serializer
    """
    project_owner = ProfileMiniSerializer(source='owner', read_only=True)
    created_by = ProfileMiniSerializer(read_only=True)
    updated_by = ProfileMiniSerializer(read_only=True)
    project_status = serializers.SerializerMethodField('get_project_status_detail')

    def get_project_status_detail(self, obj):
        return [item[1] for item in Project.PROJECT_STATUS_CHOICES if item[0] == obj.status][0]

    def validate(self, attrs):
        view = self.context.get('view')
        attrs['status'] = Project.BASIC
        attrs['owner'] = view.request.user
        attrs['updated_by'] = view.request.user
        if view.request.method == "DELETE":
            attrs['destroyed_by'] = view.request.user
        return attrs

    class Meta:
        model = Project
        fields = (
            'id', 'name', 'description', 'city', 'state', 'country', 'org_name', 'project_type',
            'poc_name', 'poc_contact', 'poc_email', 'poc_designation', 'created_by',
            'updated_by', 'created_at', 'updated_at', 'project_owner', 'zipcode', 'project_status')
        # extra_kwargs = {
        #     'status': {'write_only': True},
        #     'owner': {'write_only': True}
        # }


class ProjectSpecificDetailSerializer(serializers.ModelSerializer):
    """
    serializer for project specific apis
    """
    project = ProjectSerializer(read_only=True)

    def validate(self, attrs):
        view = self.context.get('view')
        project = get_object_or_404(Project, pk=view.kwargs[view.lookup_url_kwargs])
        attrs['project'] = project
        total = attrs.get('turbine_elec', 0.00) + attrs.get('chp_elec') + attrs.get('high_efficiency_gas_elec') + attrs.get('local_other_gas_elec') + attrs.get('wind_solar_pv_elec') + attrs.get('biomass_elec') + attrs.get('geothermal_elec') + attrs.get('other_local_elec')
        attrs['turbine_elec'] = (attrs['turbine_elec']/total)*100
        attrs['chp_elec'] = (attrs['chp_elec']/total)*100
        attrs['high_efficiency_gas_elec'] = (attrs['high_efficiency_gas_elec']/total)*100
        attrs['local_other_gas_elec'] = (attrs['local_other_gas_elec']/total)*100
        attrs['wind_solar_pv_elec'] = (attrs['wind_solar_pv_elec']/total)*100
        attrs['biomass_elec'] = (attrs['biomass_elec']/total)*100
        attrs['geothermal_elec'] = (attrs['geothermal_elec']/total)*100
        attrs['other_local_elec'] = (attrs['other_local_elec']/total)*100
        return attrs

    class Meta:
        model = ProjectSpecificInfo
        fields = (
            'project', 'res_customer', 'comm_industrial1', 'comm_industrial2', 'annual_customer_load',
            'customer_hr_peak_demand', 'annual_purchased_elec', 'purchased_hr_peak_demand',
            'tnd_losses', 'tot_local_elec_generation', 'turbine_elec', 'chp_elec', 'high_efficiency_gas_elec',
            'local_other_gas_elec', 'wind_solar_pv_elec', 'biomass_elec', 'geothermal_elec',
            'other_local_elec', 'tot_local_generation_capacity', 'turbine_elec_capacity',
            'chp_elec_capacity', 'high_efficiency_gas_elec_capacity', 'local_other_gas_elec_capacity',
            'wind_solar_pv_elec_capacity', 'biomass_elec_capacity', 'geothermal_elec_capacity',
            'other_local_elec_capacity', 'electricity_unit', 'thermal_unit', 'currency')


class CreditsAchievedSerializer(serializers.ModelSerializer):
    """
    CreditsAchievedSerializer
    """
    class Meta:
        model = CreditsAchieved


class StrategySerializer(serializers.ModelSerializer):
    """
    StrategySerializer
    """
    class Meta:
        model = Strategy


class StrategyQuestionSerializer(serializers.ModelSerializer):
    """
    StrategyQuestionSerializer
    """
    class Meta:
        model = StrategyQuestion


class ProjectQuestionSerializer(serializers.ModelSerializer):
    """
    ProjectQuestionSerializer
    """
    submitted_by = ProfileMiniSerializer(read_only=True)
    question = StrategyQuestionSerializer(read_only=True)
    project = ProjectMiniSerializer(read_only=True)

    def validate(self, attrs):
        view = self.context.get('view')
        project = get_object_or_404(Project, pk=view.kwargs[view.lookup_url_kwargs])
        question = get_object_or_404(StrategyQuestion, pk=view.kwargs[view.lookup_field])
        attrs['project'] = project
        attrs['question'] = question
        attrs['submitted_by'] = view.request.user
        return attrs

    class Meta:
        model = ProjectQuestion
        read_only_fields = ('project', 'question', 'submitted_by')
