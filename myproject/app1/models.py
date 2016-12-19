from __future__ import unicode_literals

from django.db import models

class Snippet(models.Model):
	owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
	name=models.CharField(max_length=10)
	address=models.CharField(max_length=10)
	dob=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name


