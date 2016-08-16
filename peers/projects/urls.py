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
]
