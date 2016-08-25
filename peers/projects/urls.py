from django.conf.urls import url
from projects import apis

urlpatterns = [
    url(r'^$', apis.ProjectApi.as_view(), name="api_projects"),
    url(r'^(?P<pk>\d+)/$', apis.ProjectDetail.as_view(), name="api_project_detail"),
    url(r'^(?P<pk>\d+)/specific/information/$', apis.ProjectSpecificDetail.as_view(), name="api_project_specific_detail"),
    url(r'^(?P<project_pk>\d+)/credits/$', apis.CreditsAchievedListApi.as_view(), name="api_project_credits"),
    url(r'^credit/(?P<credit_pk>\d+)/strategy/$', apis.StrategyApi.as_view(), name="api_credits_strategy"),
    url(r'^strategy/(?P<strategy_pk>\d+)/questions/$', apis.StrategyQuestionApi.as_view(), name="api_strategy_questions"),
    url(r'^(?P<project_pk>\d+)/strategy/(?P<strategy_unique>.*)/$', apis.ProjectStrategyApi.as_view(), name="api_project_question"),
    url(r'^(?P<project_pk>\d+)/plant/$', apis.ProjectPlantApi.as_view(), name="api_project_plant"),
    url(r'^(?P<project_pk>\d+)/plant/(?P<plant_pk>\d+)/$', apis.ProjectPlantDetail.as_view(), name="api_project_plant_update"),
    url(r'^(?P<project_pk>\d+)/sei/calculate/$', apis.ProjectSEI.as_view(), name="api_project_sei"),
    url(r'^(?P<project_pk>\d+)/score/calculate/$', apis.ProjectScore.as_view(), name="api_project_score"),
    url(r'^(?P<project_pk>\d+)/lre/score/calculate/$', apis.LREStrategyScore.as_view(), name="api_lre_score"),
    url(r'^electricity/plants/$', apis.ElectricityPlantList.as_view(), name="api_electricity_plant"),

]
