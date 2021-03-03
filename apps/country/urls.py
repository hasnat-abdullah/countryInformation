from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('country/<int:pk>', CountryDetailView.as_view(), name="country_details"),
]