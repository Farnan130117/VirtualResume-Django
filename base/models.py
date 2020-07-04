from django.db import models
from datetime import datetime 

# Create your models here.


class project(models.Model):     #project_class

	name = models.CharField(max_length=200, null=True)
	gitrepo = models.CharField(max_length=200, null=True)
	picture = models.ImageField(null=True)    
	  #pip install pillow
	  #Pillow is a Python Imaging Library which deals with different image files. 
	  #We won’t be using pillow directly but Django is using it. Therefore, we need pillow library.
	date_created = models.DateTimeField(default=datetime.now(), null=True,  editable=False)
	#date_created = models.DateTimeField(auto_now_add=True, null=True)
     
	def __str__(self):
		return self.name
