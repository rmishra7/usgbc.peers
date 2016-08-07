from django.conf.urls import url
from projects import apis

urlpatterns = [
    url(r'^$', apis.ProjectApi.as_view(), name="api_projects"),
    url(r'^(?P<pk>\d+)/$', apis.ProjectDetail.as_view(), name="api_project_detail"),
]
