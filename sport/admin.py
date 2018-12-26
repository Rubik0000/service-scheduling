from django.contrib import admin

# Register your models here.

from .models import WeekDay, ExerciseType, Trainer, Exercise

admin.site.register(WeekDay)
admin.site.register(ExerciseType)
admin.site.register(Trainer)
admin.site.register(Exercise)