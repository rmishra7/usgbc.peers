
from django.conf.urls import url
from home import apis

urlpatterns = [
    url(r'^countries/$', apis.CountriesApi.as_view(), name="api_countries_list"),
    url(r'^states/$', apis.StatesApi.as_view(), name="api_states_list"),
    # url(r'^$', views.HomeView.as_view(), name="home"),
    # url(r'^project/submit-project/$', views.ProjectGeneralView.as_view(), name="dashboard_view"),
    # url(r'^project/(?P<project_id>\d+)/information/$', views.ProjectSpecificView.as_view(), name="dashboard_view"),
]
