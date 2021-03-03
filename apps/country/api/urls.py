from django.urls import path, include
from .views import *

'''country apps API url patterns'''
urlpatterns = [
    path('countries/', CountryListCreateAPIView.as_view()),
    path('countries/<int:id>', CountryGetDeleteUpdateAPIView.as_view()),
    path('countries/<int:id>/neighbour/', NeighbouringCountriesAPIView.as_view()),
    path('countries/search/', SearchCountriesAPIView.as_view()),
    path('get_token/', UserToken.as_view()),
]
