# profile/urls.py
from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('view/', views.view_profile, name='view_profile'),
    path('update/', views.ProfileUpdateView.as_view(), name='update_profile'),
]
