from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('error', views.error, name='error'),
    path('login',views.login, name='login'),
]