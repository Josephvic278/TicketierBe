from django.urls import path
from .views import RegisterView, MeView, DeviceRegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('me/', MeView.as_view(), name='auth_me'),
    path('device-register/', DeviceRegisterView.as_view(), name='device_register'),
]
