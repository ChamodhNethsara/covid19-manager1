from django.contrib import admin
from .models import Patient
# Register your models here.

@admin.register(Patient)
class PostAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','tested_date','status')
    list_filter =('tested_date','status')