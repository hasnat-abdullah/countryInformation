from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR)
from apps.country.models import CountryInfo
from apps.country.serializer import CountryModelSerializer
from logs.log import Log

def prepare_error_response(message):
    """
    get error message and return error response
    :param details:
    :return:
    """
    response = {
        'type': 'error',
        'message': message,
        "data": None
    }
    return response


def prepare_success_response(message,data):
    """
    receive success data to retun success response
    :param message:
    :param data:
    :return:
    """
    response = {
        'type': 'success',
        'message': message,
        'data': data
    }
    return response


class CountryListCreateAPIView(generics.ListCreateAPIView):
    """return All country list view order by name and also insert a country info instance. """
    serializer_class = CountryModelSerializer

    def get_queryset(self):
        return CountryInfo.objects.all().order_by('name')


class CountryGetDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """get, update and delete a specific country"""
    serializer_class = CountryModelSerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return CountryInfo.objects.all()

        