from django.utils.translation import ugettext_lazy as _

from rest_framework import generics, response, status, serializers

from .countries import countries_list
from .states import states


class CountriesApi(generics.GenericAPIView):
    """
    return list of countries
    """
    def get(self, request, *args, **kwargs):
        return response.Response(countries_list, status=status.HTTP_200_OK)


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
