"""
URL configuration for ProyectoEsp8266 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from importlib.resources import path
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/', views.salir, name="salir"),
    path('', views.control_led, name='control_led'),  # Página principal con botones
    path('encender/', views.encender_led, name='encender_led'),
    path('apagar/', views.apagar_led, name='apagar_led'),
]