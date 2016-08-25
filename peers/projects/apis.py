from __future__ import division
from django.shortcuts import get_object_or_404
from django.db.models import Sum

from rest_framework import generics, status, response, permissions, serializers
import uuid
from decimal import Decimal

from .constants import national_sei
from .models import (
    Project, ProjectStrategy, CreditsAchieved, Strategy, StrategyQuestion,
    ProjectSpecificInfo, ProjectPlant, ElectricityPlant)
from .serializers import (
    ProjectSerializer, ProjectDetailSerializer, ProjectStrategySerializer,
    CreditsAchievedSerializer, StrategySerializer, StrategyQuestionSerializer,
    ProjectSpecificDetailSerializer, ProjectPlantSerializer, ElectricityPlantSerializer,
    ProjectPlantDetailSerializer
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


class ProjectStrategyApi(generics.CreateAPIView):
    """
    api to save answered data on a strategy's question by user
    """
    model = ProjectStrategy
    page_size = 10
    serializer_class = ProjectStrategySerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_url_kwargs = "project_pk"
    lookup_field = "strategy_unique"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()


class ProjectPlantApi(generics.ListCreateAPIView):
    """
    api to list/create project plant entry
    """
    model = ProjectPlant
    page_size = 10
    serializer_class = ProjectPlantSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_url_kwargs = "project_pk"
    queryset = model.objects.all()

    def get_queryset(self):
        project = get_object_or_404(Project, pk=self.kwargs[self.lookup_url_kwargs])
        return self.queryset.filter(project=project)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()


class ProjectPlantDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    to retrieve, update and delete project selected plant
    """
    model = ProjectPlant
    page_size = 10
    serializer_class = ProjectPlantDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_url_kwargs = "project_pk"
    lookup_field = "plant_pk"

    def get_object(self):
        get_object_or_404(Project, pk=self.kwargs[self.lookup_url_kwargs])
        instance = get_object_or_404(self.model, pk=self.kwargs[self.lookup_field])
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


class ElectricityPlantList(generics.ListAPIView):
    """
    api to return list of electricity plants
    """
    model = ElectricityPlant
    page_size = 10
    serializer_class = ElectricityPlantSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = model.objects.all()

    def get_queryset(self):
        kwargs = {}
        for k, vals in self.request.GET.lists():
            for v in vals:
                kwargs[k] = v
        if not kwargs:
            return self.queryset
        return self.queryset.filter(**kwargs)


class ProjectSEI(generics.GenericAPIView):
    """
    api to calculate sei value
    """
    lookup_url_kwargs = "project_pk"
    queryset = ""

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs[self.lookup_url_kwargs])
        project_info = project.project_specific.get()
        tnd = 1 + float(project_info.tnd_losses/100)
        value = 0
        if project.project_specific.get().payment_option == "scr":
            if project_info.bulk_coal != 0:
                sei_c = national_sei[project.country]["coal"] * float(project_info.bulk_coal)
                value = value + sei_c
            if project_info.bulk_petroleum != 0:
                sei_p = national_sei[project.country]["petroleum"] * float(project_info.bulk_petroleum)
                value = value + sei_p
            if project_info.bulk_simple_gas != 0:
                sei_sg = national_sei[project.country]["simple-gas"] * float(project_info.bulk_simple_gas)
                value = value + sei_sg
            if project_info.bulk_high_eff_gas != 0:
                sei_bhg = national_sei[project.country]["gas"] * float(project_info.bulk_high_eff_gas)
                value = value + sei_bhg
            if project_info.bulk_nuclear != 0:
                sei_n = national_sei[project.country]["nuclear"] * float(project_info.bulk_nuclear)
                value = value + sei_n
            if project_info.chp_elec != 0:
                sei_cg = national_sei[project.country]["chp-gas"] * float(project_info.chp_elec)
                value = value + sei_cg
            if project_info.high_efficiency_gas_elec != 0:
                sei_hg = national_sei[project.country]["gas"] * float(project_info.high_efficiency_gas_elec)
                value = value + sei_hg
            sei = (value/(project_info.tot_local_elec_generation + project_info.annual_purchased_elec)) * float(tnd)
        elif project.project_specific.get().payment_option == "ppp":
            plant = ProjectPlant.objects.filter(project=project)
            thermal = plant.aggregate(Sum('thermal_energy'))
            tot_energy = 0
            for p in plant:
                elec = float(p.sei_value)*float(p.electricity_delivered)
                tot_energy = tot_energy + elec
            sei = (float(tot_energy) - float(thermal['thermal_energy__sum']))/float(project_info.tot_local_elec_generation + project_info.annual_purchased_elec)
        else:
            raise serializers.ValidationError("No Payment Option is provided for project.")
        TWOPLACES = Decimal(10) ** -2
        sei = Decimal(sei).quantize(TWOPLACES)
        project_info.project_sei = sei
        project_info.save()
        response_data = {
            'sei': sei
        }
        return response.Response(response_data, status=status.HTTP_200_OK)


class SEIStrategyScore(generics.GenericAPIView):
    """
    api to calculate score of project
    """
    lookup_url_kwargs = "project_pk"

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs[self.lookup_url_kwargs])
        project_info = project.project_specific.get()
        print "project_info.project_sei", project_info.project_sei
        if project_info.project_sei <= 5:
            sei_score = 50
        elif 5 < project_info.project_sei <= 12.5:
            sei_score = 50 - (20/3) * (float(project_info.project_sei) - 5)
        else:
            sei_score = 0
        TWOPLACES = Decimal(10) ** -2
        sei_score = Decimal(sei_score).quantize(TWOPLACES)
        project_info.sei_score = sei_score
        project_info.save()
        response_data = {
            "score": sei_score
        }
        return response.Response(response_data, status=status.HTTP_200_OK)


class LREStrategyScore(generics.GenericAPIView):
    """
    lre score calculation
    """
    lookup_url_kwargs = "project_pk"

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs[self.lookup_url_kwargs])
        project_info = project.project_specific.get()
        if project.project_type == Project.CITY or project.project_type == Project.CAMPUS:
            if 0 < project_info.customer_elec_load_supplied <= 5:
                lre_score = 1
            else:
                lre_score = 5
        else:
            if 0 < project_info.customer_elec_load_supplied <= 5:
                lre_score = 1
            else:
                lre_score = 3
        project_info.lre_score = lre_score
        project_info.save()
        response_data = {
            'lre_score': lre_score
        }
        return response.Response(response_data, status=status.HTTP_200_OK)


class OECreditScore(generics.GenericAPIView):
    """
    api to calculate score for operational effectiveness credit
    """
    lookup_url_kwargs = "project_pk"

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs[self.lookup_url_kwargs])
        project_info = project.project_specific.get()
        bulk_sei = 10.27
        total_energy = project_info.annual_purchased_elec + project_info.tot_local_elec_generation
        sei = bulk_sei - project_info.project_sei
        ees = sei * total_energy * project_info.annual_fuel_cost
        if project.project_type == Project.CITY:
            if ees <= 0:
                oe_credit_score = 0
            else:
                oe_credit_score = 9
        else:
            if ees <= 0:
                oe_credit_score = 0
            else:
                oe_credit_score = 5
        project_info.bulk_sei = bulk_sei
        project_info.ees_value = ees
        project_info.oe_credit_score = oe_credit_score
        project_info.save()
        response_data = {
            "ees_value": ees,
            "oe_credit_score": oe_credit_score
        }
        return response.Response(response_data, status=status.HTTP_200_OK)


class ProjectScore(generics.GenericAPIView):
    """
    api to calculate project score
    """
    lookup_url_kwargs = "project_pk"

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs[self.lookup_url_kwargs])
        project_info = project.project_specific.get()
        project_score = project_info.sei_score + project_info.lre_score + project_info.net_metering_score + project_info.oe_credit_score
        project_info.project_score = project_score
        project_info.save()
        response_data = {
            "project_score": project_score
        }
        return response.Response(response_data, status=status.HTTP_200_OK)
