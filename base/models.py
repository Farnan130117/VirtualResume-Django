from django.db import models

# Create your models here.

class project(models.Model):
	name = models.CharField(max_length=200, null=True)
	gitrepo = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name
