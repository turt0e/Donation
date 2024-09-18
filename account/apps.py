# account/urls.py
from django.urls import path
from . import views

app_name = 'account'  # This is needed to use the 'namespace' in include()

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    # Add other URL patterns here
]
