"""IMAC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #Path Buat admin
    path('home/', include('mainweb.urls')), #Path buat aplikasi IMAC
    path('', RedirectView.as_view(url='home/', permanent=True)), #Path klo ada org nulis langsung alamat site nde browser
    path('accounts/', include('django.contrib.auth.urls')), #Path account, deprecated, account semua lewat home sekarang
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #Path buat static (css, gambar dll)

handler404 = "mainweb.views.handle_not_found"