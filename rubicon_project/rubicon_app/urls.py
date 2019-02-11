from django.urls import path

from . import views

app_name = 'rubicon_app'
urlpatterns = [
    path('', views.index, name='index'),
]
