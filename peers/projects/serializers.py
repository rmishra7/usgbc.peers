
from rest_framework import serializers

from .models import Project
from accounts.serializers import ProfileMiniSerializer


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
            'id', 'name', 'description', 'city', 'state', 'country', 'org_name', 'org_address',
            'poc_name', 'poc_contact', 'poc_email', 'poc_designation', 'created_by',
            'updated_by', 'created_at', 'updated_at', 'project_owner', 'project_status', 'zipcode')


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
            'id', 'name', 'description', 'city', 'state', 'country', 'org_name', 'org_address', 'project_type',
            'poc_name', 'poc_contact', 'poc_email', 'poc_designation', 'created_by',
            'updated_by', 'created_at', 'updated_at', 'project_owner', 'zipcode')
        # extra_kwargs = {
        #     'status': {'write_only': True},
        #     'owner': {'write_only': True}
        # }
