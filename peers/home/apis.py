
from rest_framework import generics, response, status

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
    return list of states
    """
    def get(self, request, *args, **kwargs):
        country_code = self.request.query_params.get('country_code', None)
        result = states[country_code]
        response_data = {
            "states": result
        }
        return response.Response(response_data, status=status.HTTP_200_OK)
