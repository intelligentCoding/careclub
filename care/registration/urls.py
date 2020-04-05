#bring in the path

from django.urls import path

#bring in the views

from . import views

urlpatterns = [
    path('', views.register, name='register')
    ]