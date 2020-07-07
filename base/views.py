from django.shortcuts import render, redirect
from .models import *
from .form import projectCreate


# Create your views here.
def home(request):
	return render(request, 'base/home.html')

def vlog(request):
    return render(request, 'base/vlog.html')

def projects(request):
	projects = project.objects.all()
	return render(request, 'base/projects.html', {'projects':projects})
	
# we can upload new project in upload section
def upload(request):
    upload = projectCreate()
    if request.method == 'POST':
        upload = projectCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('/')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'base/upload_project_form.html', {'upload_form':upload})
