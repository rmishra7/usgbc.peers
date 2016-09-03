from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from rest_framework import generics, response, status, serializers
import os
import json
from collections import OrderedDict

from .states import states

countriesStates_json_file = os.path.join(settings.BASE_DIR, 'home/json/countries.json')


class CountriesApi(generics.GenericAPIView):
    """
    return list of countries
    """
    def get(self, request, *args, **kwargs):
        with open(countriesStates_json_file) as json_file:
            json_data = json.load(json_file, object_pairs_hook=OrderedDict)
        return response.Response(json_data, status=status.HTTP_200_OK)


class StatesApi(generics.GenericAPIView):
    """
    return list of states based on country_code ex. /?country_code=IN
    """
    def get(self, request, *args, **kwargs):
        country_code = self.request.query_params.get('country_code', None)
        if country_code is None:
            raise serializers.ValidationError({"Error": "Country Code is not provided."})
        result = states[country_code]
        response_data = {
            "states": result
        }
        return response.Response(response_data, status=status.HTTP_200_OK)
