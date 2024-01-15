from django.urls import path
from . import views

app_name = 'stockholm_maps'
urlpatterns = [
    path('', views.addName, name='stockholm_maps'),
]