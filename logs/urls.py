from django.urls import path
from .views import LogAPIView

urlpatterns = [
    path('<str:date_n_type>', LogAPIView.as_view(), name='log_api_view'),
]