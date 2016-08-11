from django.conf.urls import url
from accounts import apis

from accounts import views

urlpatterns = [
    url(r'^register/$', apis.Register.as_view(), name="api_register"),
    url(r'^login/$', apis.Login.as_view(), name="api_login"),
    url(r'^logout/$', apis.LogOut.as_view(), name='api_logout'),
    url(r'^activate/(?P<username>.+)/(?P<activation_key>.+)/$', apis.UserActivation.as_view(), name="api_useractivation"),
    url(r'^users/$', apis.UserList.as_view(), name="api_filter_users"),
]
