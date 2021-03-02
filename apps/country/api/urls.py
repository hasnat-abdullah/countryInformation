from django.urls import path, include
from .views import CountryListAPIView, CountryDetailsAPIView

'''country apps API url patterns'''
urlpatterns = [
    path('countries/', CountryListAPIView.as_view()),
    path('country/<int:id>', CountryDetailsAPIView.as_view()),
]
