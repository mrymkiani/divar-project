from django.contrib import admin 
<<<<<<< HEAD
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




=======
from .models import  Ad , Category
# Register your models here.
admin.site.register(Ad)
admin.site.register(Category)
# @admin.register (Ad)
# class AdAdmin(admin.ModelAdmin): ...
>>>>>>> 2908150b93fe6c7e4255bc955da488d5bab21975
