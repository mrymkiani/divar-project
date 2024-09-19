from django.contrib import admin 
from .models import  Ad , Category
# Register your models here.
admin.site.register(Ad)
admin.site.register(Category)
# @admin.register (Ad)
# class AdAdmin(admin.ModelAdmin): ...