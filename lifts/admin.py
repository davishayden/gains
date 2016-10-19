from django.contrib import admin

# Register your models here.
from .models import Lift, LiftInstance, Workout, WorkoutInstance, Cardio, CardioInstance

admin.site.register(Lift)
admin.site.register(LiftInstance)
admin.site.register(Workout)
admin.site.register(WorkoutInstance)
admin.site.register(Cardio)
admin.site.register(CardioInstance)