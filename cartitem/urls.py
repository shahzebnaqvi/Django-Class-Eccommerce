from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.cartview, name="index"),


]