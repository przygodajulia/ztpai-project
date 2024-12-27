from django.urls import path
from . import views

urlpatterns = [
    path('login-register/', views.LoginRegisterAPIView.as_view(), name='login-register'),
]