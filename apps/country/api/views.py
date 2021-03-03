from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR)
from apps.country.models import CountryInfo
from apps.country.serializer import CountryModelSerializer, NeighbouringCountryModelSerializer, LoginUserNamenSerializer
from django.db.models.query_utils import Q
# Authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
#Logger
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


def country_filtering(request):
    """filter country list based on query_param"""
    language = request.query_params.get("language", None)
    country = request.query_params.get("country", None)
    q_objects = Q()  # blank query object

    if language is not None:
        # Exact same language
        q_objects &= Q(languages__contains=[{"name": language}])  # 'and' the Q objects together

    if country is not None:
        # search by Exact or partial country name
        q_objects &= Q(name__icontains=country)  # 'and' the Q objects together
    return q_objects


class SearchCountriesAPIView(APIView):
    """Search countris by its exact or partial name and exact language"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,]

    def get(self, request,  *args, **kwargs):
        """
        :param request:
        :param args: language, country
        :param kwargs:
        :return: searched country
        """
        try:
            query_object = country_filtering(request)
            if len(query_object) < 1:
                # logger
                Log.error("Query params didn't provide.", request)
                return Response(prepare_error_response(message="Query params didn't provide."), status=HTTP_400_BAD_REQUEST)

            obj = CountryInfo.objects.filter(query_object)
            serializer = CountryModelSerializer(obj, context={'request': request}, many=True)

            # logger
            Log.info("Successfully returned", request)
            return Response(prepare_success_response(message="Successfully returned", data=serializer.data), status=HTTP_200_OK)
        except Exception as ex:
            # logger
            Log.error(str(ex),request)
            return Response(prepare_error_response(message=str(ex)), status=HTTP_500_INTERNAL_SERVER_ERROR)


class CountryListCreateAPIView(generics.ListCreateAPIView):
    """return All country list view order by name and also insert a country info instance."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,]

    serializer_class = CountryModelSerializer

    def get_queryset(self):
        return CountryInfo.objects.all().order_by('name')


class CountryGetDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """get, update and delete a specific country"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,]

    serializer_class = CountryModelSerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return CountryInfo.objects.all()


class NeighbouringCountriesAPIView(generics.RetrieveAPIView):
    """get, update and delete a specific country"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,]

    serializer_class = NeighbouringCountryModelSerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return CountryInfo.objects.all()


class UserToken(APIView):
    """ generate token to hit api  """

    def post(self, request, format=None):
        """
        Return auth token
        """
        try:
            serializer = LoginUserNamenSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.validated_data["username"]
                password = serializer.validated_data["password"]
                auth = authenticate(username=username, password=password)

                if auth is not None:
                    try:
                        refresh = RefreshToken.for_user(auth)
                        token = str(refresh.access_token)
                        data= {
                            "token": token
                        }
                        # logger
                        Log.info(f"success | Authentication success", request)
                        return Response(prepare_success_response(message="Authentication successfull",data=data), status=HTTP_200_OK)
                    except Exception as ex:
                        # logger
                        Log.error(ex, request)
                        response_param = {"message": "Token generation failed", "data": {},
                                          "type": "error"}
                        return Response(response_param, status=HTTP_200_OK)

                else:
                    # logger
                    Log.error(f"error | Employee id or password mistmatch", request)
                    return Response(prepare_error_response("'Employee id' or 'Password' Mismatch"),
                                    status=HTTP_400_BAD_REQUEST)

            else:
                # logger
                Log.error(f"error | Plz enter correct data.", request)
                return Response(prepare_error_response("Plz, enter correct data."), status=HTTP_400_BAD_REQUEST)

        except Exception as ex:
            Log.error(ex, request)
            return Response(
                {"message": "Internal server error", "data": None, "type": "error"},
                status=HTTP_500_INTERNAL_SERVER_ERROR
            )

