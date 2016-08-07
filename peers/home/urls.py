
from django.conf.urls import url
from django.views.generic.base import TemplateView

from braces.views import LoginRequiredMixin

from home import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^dashboard/$', views.DashboardView.as_view(), name="dashboard_view"),
    # url(r'^account/activate/(?P<username>.+)/(?P<activation_key>.+)/$', views.UserActivation.as_view(), name="useractivation_view"),
]
