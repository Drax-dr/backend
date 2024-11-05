from django.contrib import admin
from django.urls import include, path
from .api import api
from backend.users import views

urlpatterns = [
    path('login/', view=views.LoginView),
    path("api/v1/", api.urls)
]
