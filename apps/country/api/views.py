from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR)
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


class CountryListAPIView(generics.ListAPIView):
    serializer_class = CountryModelSerializer

    def get_queryset(self):
        return CountryInfo.objects.all().order_by('name')


class CountryDetailsAPIView(APIView):

    def get(self, request, id):
        try:
            obj = CountryInfo.objects.get(id=id)
            serializer = CountryModelSerializer(obj, context={'request': request})
            # logger
            Log.info("Successfully returned", request)
            return Response(prepare_success_response(message="Successfully returned", data=serializer.data), status=HTTP_200_OK)
        except CountryInfo.DoesNotExist:
            # logger
            Log.error("Country ID not exist.",request)
            return Response(prepare_error_response(message="Country ID not exist."), status=HTTP_404_NOT_FOUND)
        except Exception as ex:
            # logger
            Log.error(str(ex),request)
            return Response(prepare_error_response(message=str(ex)), status=HTTP_500_INTERNAL_SERVER_ERROR)