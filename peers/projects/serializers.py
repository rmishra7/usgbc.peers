
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
	fields = '__all__'


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
    project = ProjectMiniSerializer(read_only=True)

    def validate(self, attrs):
        view = self.context.get('view')
        project = get_object_or_404(Project, pk=view.kwargs[view.lookup_url_kwargs])
        attrs['project'] = project
        if 'bulk_coal' not in attrs:
            attrs['bulk_coal'] = 0
        if 'bulk_petroleum' not in attrs:
            attrs['bulk_petroleum'] = 0
        if 'bulk_simple_gas' not in attrs:
            attrs['bulk_simple_gas'] = 0
        if 'bulk_high_eff_gas' not in attrs:
            attrs['bulk_high_eff_gas'] = 0
        if 'bulk_hydro' not in attrs:
            attrs['bulk_hydro'] = 0
        if 'bulk_nuclear' not in attrs:
            attrs['bulk_nuclear'] = 0
        if 'bulk_solar_pv_wind' not in attrs:
            attrs['bulk_solar_pv_wind'] = 0
        return attrs

    class Meta:
        model = ProjectSpecificInfo
	fields = '__all__'


class CreditsAchievedSerializer(serializers.ModelSerializer):
    """
    CreditsAchievedSerializer
    """
    class Meta:
        model = CreditsAchieved
	fields = '__all__'


class StrategySerializer(serializers.ModelSerializer):
    """
    StrategySerializer
    """
    class Meta:
        model = Strategy
	fields = '__all__'


class StrategyQuestionSerializer(serializers.ModelSerializer):
    """
    StrategyQuestionSerializer
    """
    class Meta:
        model = StrategyQuestion
	fields = '__all__'


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
	fields = '__all__'
        read_only_fields = ('project', 'strategy', 'submitted_by')


class ProjectPlantSerializer(serializers.ModelSerializer):
    """
    serializer for project plant
    """
    project = ProjectMiniSerializer(read_only=True)

    def validate(self, attrs):
        view = self.context.get('view')
        project = get_object_or_404(Project, pk=view.kwargs[view.lookup_url_kwargs])
        plant = get_object_or_404(ElectricityPlant, pk=attrs['plant_name'])
        attrs['plant_name'] = plant.plant_name
        attrs['project'] = project
        attrs['country'] = project.country
        attrs['sei_value'] = plant.sei_value
        return attrs

    class Meta:
        model = ProjectPlant
        read_only_fields = ('country', 'sei_value')
        exclude = ('delete', )


class ProjectPlantDetailSerializer(serializers.ModelSerializer):
    """
    serializer for project plant
    """
    project = ProjectMiniSerializer(read_only=True)

    class Meta:
        model = ProjectPlant
        read_only_fields = ('country', 'sei_value', 'plant_name')
        exclude = ('delete', )


class ElectricityPlantSerializer(serializers.ModelSerializer):
    """
    electricity plant serializer
    """
    class Meta:
        model = ElectricityPlant
	fields = '__all__'


class ProjectScoreSerializer(serializers.Serializer):
    """
    serializer for project score
    """
    score = serializers.CharField()
