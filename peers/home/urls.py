
from django.conf.urls import url
from django.views.generic.base import TemplateView

from braces.views import LoginRequiredMixin

from home import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^project/submit-project/$', views.ProjectGeneralView.as_view(), name="dashboard_view"),
    url(r'^project/(?P<project_id>\d+)/information/$', views.ProjectSpecificView.as_view(), name="dashboard_view"),
    url(r'^account/activate/(?P<username>.+)/(?P<activation_key>.+)/$', views.UserActivation.as_view(), name="useractivation_view"),
]
