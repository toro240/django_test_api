from django.contrib import admin
from .models import Diary


@admin.register(Diary)
class Diary(admin.ModelAdmin):
    pass
