from .views import *
from django.urls import path
urlpatterns = [
    path("MyAds", MyAds.as_view()),
    path("EditAds/<int:pk>", EditAd.as_view()),
    path("ViewAds", ViewAd.as_view()),]