from django.urls import path
from generator.views import create_certificate
from . import views

urlpatterns = [
    path('', create_certificate, name='create_certificate'),
]
