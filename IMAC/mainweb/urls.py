from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('error', views.error, name='error'),
    path('login',views.user_login, name='customlogin'),
    path('recruitment2023',views.admitted, name='admitted'),
    path('signup',views.register, name='customsignup'),
    path('find-your-manager', views.your_manajer, name = 'yourmanajer')
]