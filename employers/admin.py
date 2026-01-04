from django.contrib import admin
from .models import EmployerProfile


@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'location')
    search_fields = ('company_name', 'user__username')
