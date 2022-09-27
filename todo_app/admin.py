from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class AdminToDo(admin.ModelAdmin):
    list_display = ('text', 'completed')
