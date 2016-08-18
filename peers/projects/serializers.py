
from django.shortcuts import get_object_or_404

from rest_framework import serializers

from .models import (
    Project, ProjectStrategy, StrategyQuestion, CreditsAchieved, Strategy,
    ProjectSpecificInfo, ProjectPlant, ElectricityPlant)
from accounts.serializers import ProfileMiniSerializer
from .constants import national_sei


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
            'id', 'name', 'description', 'city', 'state', 'country', 'org_name', 'region',
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
            'poc_name', 'poc_contact', 'poc_email', 'poc_designation', 'created_by', 'region',
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
        turbine_elec = attrs.get('turbine_elec') if attrs.get('turbine_elec') is not None else project.project_specific.get().turbine_elec
        chp_elec = attrs.get('chp_elec') if attrs.get('chp_elec') is not None else project.project_specific.get().chp_elec
        high_efficiency_gas_elec = attrs.get('high_efficiency_gas_elec') if attrs.get('high_efficiency_gas_elec') is not None else project.project_specific.get().high_efficiency_gas_elec
        local_other_gas_elec = attrs.get('local_other_gas_elec') if attrs.get('local_other_gas_elec') is not None else project.project_specific.get().local_other_gas_elec
        wind_solar_pv_elec = attrs.get('wind_solar_pv_elec') if attrs.get('wind_solar_pv_elec') is not None else project.project_specific.get().wind_solar_pv_elec
        biomass_elec = attrs.get('biomass_elec') if attrs.get('biomass_elec') is not None else project.project_specific.get().biomass_elec
        geothermal_elec = attrs.get('geothermal_elec') if attrs.get('geothermal_elec') is not None else project.project_specific.get().geothermal_elec
        other_local_elec = attrs.get('other_local_elec') if attrs.get('other_local_elec') is not None else project.project_specific.get().other_local_elec
        total = turbine_elec + chp_elec + high_efficiency_gas_elec + local_other_gas_elec + wind_solar_pv_elec + biomass_elec + geothermal_elec + other_local_elec
        if total == 0:
            total = 1
        attrs['turbine_elec'] = (turbine_elec/total)*100
        attrs['chp_elec'] = (chp_elec/total)*100
        attrs['high_efficiency_gas_elec'] = (high_efficiency_gas_elec/total)*100
        attrs['local_other_gas_elec'] = (local_other_gas_elec/total)*100
        attrs['wind_solar_pv_elec'] = (wind_solar_pv_elec/total)*100
        attrs['biomass_elec'] = (biomass_elec/total)*100
        attrs['geothermal_elec'] = (geothermal_elec/total)*100
        attrs['other_local_elec'] = (other_local_elec/total)*100
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
            'other_local_elec_capacity', 'electricity_unit', 'thermal_unit', 'currency',
            'frequency_range', 'customer_served', 'project_sei', 'payment_option', 'bulk_coal',
            'bulk_petroleum', 'bulk_simple_gas', 'bulk_high_eff_gas', 'bulk_hydro', 'bulk_nuclear',
            'bulk_solar_pv_wind')


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


class ProjectStrategySerializer(serializers.ModelSerializer):
    """
    ProjectQuestionSerializer
    """
    submitted_by = ProfileMiniSerializer(read_only=True)
    question = StrategyQuestionSerializer(read_only=True)
    project = ProjectMiniSerializer(read_only=True)

    def validate(self, attrs):
        view = self.context.get('view')
        project = get_object_or_404(Project, pk=view.kwargs[view.lookup_url_kwargs])
        strategy = get_object_or_404(Strategy, unique_id=view.kwargs[view.lookup_field])
        attrs['project'] = project
        attrs['strategy'] = strategy
        attrs['submitted_by'] = view.request.user
        return attrs

    class Meta:
        model = ProjectStrategy
        read_only_fields = ('project', 'strategy', 'submitted_by')


class ProjectPlantSerializer(serializers.ModelSerializer):
    """
    serializer for project plant
    """
    project = ProjectMiniSerializer(read_only=True)

    def validate(self, attrs):
        view = self.context.get('view')
        project = get_object_or_404(Project, pk=view.kwargs[view.lookup_url_kwargs])
        attrs['project'] = project
        attrs['country'] = project.country
        attrs['sei_value'] = national_sei[project.country][attrs['fuel_type']]
        return attrs

    class Meta:
        model = ProjectPlant
        read_only_fields = ('country', 'sei_value')
        exclude = ('delete', )


class ElectricityPlantSerializer(serializers.ModelSerializer):
    """
    electricity plant serializer
    """
    class Meta:
        model = ElectricityPlant
