
from django.shortcuts import get_object_or_404

from rest_framework import generics, status, response, permissions
import uuid

from .models import (
    Project, ProjectQuestion, CreditsAchieved, Strategy, StrategyQuestion,
    ProjectSpecificInfo, )
from .serializers import (
    ProjectSerializer, ProjectDetailSerializer, ProjectQuestionSerializer,
    CreditsAchievedSerializer, StrategySerializer, StrategyQuestionSerializer,
    ProjectSpecificDetailSerializer,
    )
# from .tasks import project_submission_listener, project_submission_success_listener


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
        instance = Project.objects.get(uuid=uuid.UUID(serializer['uuid'].value))
        ProjectSpecificInfo.objects.create(project=instance)
        # project_submission_listener.delay(self.request.user.id)
        # project_submission_success_listener.delay(self.request.user.id)


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


class ProjectSpecificDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    api to retrieve project instance, update and destroy project instance
    """
    model = ProjectSpecificInfo
    serializer_class = ProjectSpecificDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_url_kwargs = "pk"

    def get_object(self):
        project = get_object_or_404(Project, pk=self.kwargs[self.lookup_url_kwargs])
        instance = get_object_or_404(self.model, project=project)
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


class CreditsAchievedListApi(generics.ListAPIView):
    """
    return list of all the credits
    """
    model = CreditsAchieved
    page_size = 10
    serializer_class = CreditsAchievedSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = model.objects.all()
    lookup_url_kwargs = "project_pk"

    def get_queryset(self):
        project = Project.objects.get(pk=self.kwargs[self.lookup_url_kwargs])
        kwargs = {}
        if project.project_type == Project.CITY:
            kwargs['city_credit'] = True
        elif project.project_type == Project.CAMPUS:
            kwargs['campus_credit'] = True
        else:
            kwargs['supply_credit'] = True
        return self.queryset.filter(**kwargs)


class StrategyApi(generics.ListAPIView):
    """
    return strategy based on credits
    """
    model = Strategy
    page_size = 10
    serializer_class = StrategySerializer
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = model.objects.all()
    lookup_url_kwargs = "credit_pk"

    def get_queryset(self):
        credit = get_object_or_404(CreditsAchieved, pk=self.kwargs[self.lookup_url_kwargs])
        return self.queryset.filter(credit=credit)


class StrategyQuestionApi(generics.ListAPIView):
    """
    return questions based on strategy
    """
    model = StrategyQuestion
    page_size = 10
    serializer_class = StrategyQuestionSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = model.objects.all()
    lookup_url_kwargs = "strategy_pk"

    def get_queryset(self):
        strategy = get_object_or_404(Strategy, pk=self.kwargs[self.lookup_url_kwargs])
        return self.queryset.filter(strategy=strategy)


class ProjectQuestionApi(generics.ListCreateAPIView):
    """
    api to save answered data on a strategy's question by user
    """
    model = ProjectQuestion
    page_size = 10
    serializer_class = ProjectQuestionSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = model.objects.all()
    lookup_url_kwargs = "project_pk"
    lookup_field = "question_pk"

    def get_queryset(self):
        project = Project.objects.get(pk=self.kwargs[self.lookup_url_kwargs])
        return self.queryset.filter(project=project)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
