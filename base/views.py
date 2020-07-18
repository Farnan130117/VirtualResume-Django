from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .form import projectCreate # importing projectCreate form in this file

#Register Section

def registerPage(request):
    context={}
    return render(request,'base/register.html',context)
#Login Section

def loginPage(request):
    context={}
    return render(request,'base/login.html',context)

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
    upload = projectCreate() # adding input form 
    if request.method == 'POST':
        upload = projectCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('/')
        else:
            return HttpResponse("""Your form is wrong, reload on <a href="/upload/"> Upload Project</a>""")
    else:
        return render(request, 'base/upload_project_form.html', {'upload_form':upload})


#update_project
def update_project(request, project_id):
    project_id = int(project_id)
    try:
        project_find = project.objects.get(id = project_id)
    except project.DoesNotExist:
        return redirect('projects')
    project_form = projectCreate(request.POST or None, instance = project_find)
    if project_form.is_valid():
       project_form.save()
       return redirect('projects')
    return render(request, 'base/upload_project_form.html', {'upload_form':project_form})

#Delete_project
def delete_project(request,project_id):
    project_id = int(project_id)
    try:
        project_find = project.objects.get(id = project_id)
    except project.DoesNotExist:
        return redirect('projects')
    project_find.delete()
    return redirect('projects')