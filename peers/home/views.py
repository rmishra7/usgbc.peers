
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View, base
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render
# from django.conf import settings
# from django.contrib import auth

import uuid
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin

from accounts.models import Profile


class HomeView(AnonymousRequiredMixin, base.TemplateView):
    """
    home page
    """
    authenticated_redirect_url = reverse_lazy(_('dashboard_view'))
    template_name = "index.html"


class DashboardView(LoginRequiredMixin, base.TemplateView):
    """
    dashboard view
    """
    login_url = reverse_lazy(_('home'))
    template_name = "dashboard.html"


class UserActivation(AnonymousRequiredMixin, View):
    """
    user account activation view
    """
    model = Profile
    lookup_url_kwargs = "username"
    lookup_field = "activation_key"

    def get(self, request):
        instance = get_object_or_404(self.model, username=self.kwargs[self.lookup_url_kwargs])
        if instance.account_activated is True:
            context = {
                'username': self.kwargs[self.lookup_url_kwargs],
                'activation': "Activated Account"
            }
            return render(request, 'account_activation.html', context)
        if instance.uuid != uuid.UUID(self.kwargs[self.lookup_field]):
            context = {
                'username': self.kwargs[self.lookup_url_kwargs],
                'activation': "Invalid Token"
            }
            return render(request, 'account_activation.html', context)
        instance.account_activated = True
        instance.save()
        # instance.backend = settings.AUTHENTICATION_BACKENDS[0]
        # auth.login(self.request, instance)
        context = {
            'username': self.kwargs[self.lookup_url_kwargs],
            'activation': "success"
        }
        return render(request, "account_activation.html", context)
