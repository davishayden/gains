from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
class Lift(models.Model):
	name = models.CharField(max_length=200)
	created_at = models.DateTimeField('created at')
	m_group = models.CharField(max_length=200)
	def __str__(self):
		return self.name
