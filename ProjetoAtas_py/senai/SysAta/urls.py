from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ata/',views.ata, name = 'ata'),
    path('todas/',views.todasAtas, name='todas')
]
