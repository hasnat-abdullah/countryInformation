from django.urls import path, include

'''Parent API url patterns'''
urlpatterns = [
    path('', include('apps.country.api.urls')),
]
