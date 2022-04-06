from django.urls import path
from . import views

urlpatterns = [
    path('find', views.getgeodata, name='find'),
]
