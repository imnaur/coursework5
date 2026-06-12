from django.contrib import admin
from .models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "location",
        "time",
        "is_pleasant",
        "action",
        "compensation",
        "regularity",
        "time_required",
        "public",
        "related_habit",
    )
