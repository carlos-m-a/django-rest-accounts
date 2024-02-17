from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # For API - rest framework
    path('register/', views.RegisterUserAPIView.as_view()),

    path('user/',views.UserDetailAPI.as_view()),
    path('user/change-password/', views.ChangePasswordView.as_view()),
]