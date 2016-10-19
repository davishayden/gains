from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Lift(models.Model):
	name = models.CharField(max_length=200)
	created_at = models.DateTimeField('created at')
	m_group = models.CharField(max_length=200)
	def __str__(self):
		return self.name

#Instance of a lift event
class LiftInstance(models.Model):
	created_at = models.DateTimeField('created at')
	type = models.IntegerField()
	reps = ArrayField(models.IntegerField())
	sets = ArrayField(models.IntegerField())
	weight = ArrayField(models.IntegerField())
	def __str__(self):
		return str(self.created_at)

#Type of cardio event
class Cardio(models.Model):
	name = models.CharField(max_length=200)
	created_at = models.DateTimeField('created at')
	def __str__(self):
		return self.name

#Actual Cardio event
class CardioInstance(models.Model):
	name = models.CharField(max_length=200)
	type = models.IntegerField()
	created_at = models.DateTimeField('created at')
	duration = models.FloatField()
	distance = models.FloatField()
	def __str__(self):
		return str(self.created_at)

#Work instance
class Workout(models.Model):
	name = models.CharField(max_length=200)
	created_at = models.DateTimeField('created at')
	cardio_plan = ArrayField(models.IntegerField())
	lift_plan = ArrayField(models.IntegerField())
	def __str__(self):
		return self.name

#Work instance
class WorkoutInstance(models.Model):
	name = models.CharField(max_length=200)
	created_at = models.DateTimeField('created at')
	cardio_events = ArrayField(models.IntegerField())
	lift_events = ArrayField(models.IntegerField())
	def __str__(self):
		return self.name
