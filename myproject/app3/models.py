from __future__ import unicode_literals

from django.db import models

# Create your models here.
from __future__ import unicode_literals

from django.db import models

class Snippet(models.Model):
	name=models.CharField(max_length=10)
	address=models.CharField(max_length=10)
	dob=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name