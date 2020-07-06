from django import forms
from .models import project

#Create ProjectCreate Form for project ModelForm

class projectCreate(forms.ModelForm):
	class Meta:
		model=project
		fields= '__all__'   # Approving all the fields for projectCreate form
			
		