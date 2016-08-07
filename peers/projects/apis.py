
from django.shortcuts import get_object_or_404

from rest_framework import generics, status, response, permissions

from .models import Project
from .serializers import (
    ProjectSerializer, ProjectDetailSerializer
    )
from .tasks import project_submission_listener, project_submission_success_listener


class ProjectApi(generics.ListCreateAPIView):
    """
    api to list/create projects
    """
    model = Project
    page_size = 10
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = model.objects.all()

    def get_queryset(self):
        return self.queryset.project_of_owner(self.request.user)

    def perform_create(self, serializer):
        serializer.save()
        project_submission_listener.delay(self.request.user.id)
        project_submission_success_listener.delay(self.request.user.id)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    api to retrieve project instance, update and destroy project instance
    """
    model = Project
    serializer_class = ProjectDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_url_kwargs = "pk"

    def get_object(self):
        instance = get_object_or_404(self.model, pk=self.kwargs[self.lookup_url_kwargs])
        return instance

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
