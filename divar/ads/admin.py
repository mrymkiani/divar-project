from django.contrib import admin 
from .models import  *
# Register your models here.
@admin.register (Ad)
class AdAdmin(admin.ModelAdmin): ...

@admin.register (Review)
class ReviewAdmin(admin.ModelAdmin): ...

@admin.register (SavedAd)
class SavedAdAdmin(admin.ModelAdmin): ...

@admin.register (Chat)
class ChatAdmin(admin.ModelAdmin): ...


@admin.register (Notification)
class NotificationAdmin(admin.ModelAdmin): ...




