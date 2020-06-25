from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
	return render(request, 'base/home.html')

def projects(request):
	projects = project.objects.all()
	return render(request, 'base/projects.html', {'projects':projects})
