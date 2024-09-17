from django.http.response import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.shortcuts import render
from .models import Ad
from .serializers import  Adserializer
from django.db.models import Count
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView , ListAPIView)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAdminUser, IsAuthenticated , AllowAny

class ViewAd(ListCreateAPIView) : 
    queryset = Ad.objects.all()
    serializer_class = Adserializer
    filter_backends = [DjangoFilterBackend , filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ["price", "created_at"]
    search_fields = ["title"]
    filterset_fields = ['image',"imidietly"]

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser , IsAuthenticated]
        elif self.request.method == "GET":
            self.permission_classes = [AllowAny]
        return super(ViewAd, self).get_permissions()
        
class EditAd(RetrieveUpdateDestroyAPIView) : 
    queryset = Ad.objects.all()
    serializer_class = Adserializer
    filter_backends = [DjangoFilterBackend , filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ["price", "created_at"]
    search_fields = ["title"]
    filterset_fields = ['image',"imidietly"]
    permission_classes = [IsAuthenticated]
class MyAds(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = Adserializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend , filters.SearchFilter, filters.OrderingFilte]
    ordering_fields = ["created_at"]
