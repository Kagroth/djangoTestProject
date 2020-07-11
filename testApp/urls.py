from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_dir', views.create_dir, name='create_dir')
]
