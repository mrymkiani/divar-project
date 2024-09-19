from .views import *
from django.urls import path
urlpatterns = [
    path("MyAds", MyAds.as_view()),
    path("EditAds/<int:pk>", EditAd.as_view()),
    path("ViewAds", ViewAd.as_view()),
    path ('login/' , login.as_view()) ,
    path ('refresh/' , refresh.as_view()) ,

    path('reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='review-detail'),

    path('saved_ads/', SavedAdViewSet.as_view({'get': 'list', 'post': 'create'}), name='saved-ad-list-create'),
    path('saved_ads/<int:pk>/', SavedAdViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='saved-ad-detail'),

    path('chats/', ChatViewSet.as_view({'get': 'list', 'post': 'create'}), name='chat-list-create'),
    path('chats/<int:pk>/', ChatViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='chat-detail'),

    path('notifications/', NotificationViewSet.as_view({'get': 'list', 'post': 'create'}), name='notification-list-create'),
    path('notifications/<int:pk>/', NotificationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='notification-detail'),
]
