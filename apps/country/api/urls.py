from django.urls import path, include
from .views import CountryListCreateAPIView, CountryGetDeleteUpdateAPIView

'''country apps API url patterns'''
urlpatterns = [
    path('countries/', CountryListCreateAPIView.as_view()),
    path('countries/<int:id>', CountryGetDeleteUpdateAPIView.as_view()),
]
