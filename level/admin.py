from django.contrib import admin

from level.models import *

@admin.register(Level)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'level_name', 'parent_level')
