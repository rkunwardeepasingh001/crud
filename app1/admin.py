from django.contrib import admin
from .models import Data
class DataAdmin(admin.ModelAdmin):
  list_display=['ids','name','mob','email','password','image']
admin.site.register(Data,DataAdmin)
# Register your models here.
