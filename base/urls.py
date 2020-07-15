from django.urls import path
from . import views



urlpatterns	=	[

	path('',views.home,name='home'),
	path('projects/',views.projects,name='projects'),  #viewing all projects
	path('projects/upload/',views.upload,name='upload'),  # we can upload new project in upload section
	path('projects/update/<int:project_id>', views.update_project,name='update'), # Edit project
	path('projects/delete/<int:project_id>', views.delete_project,name='delete'), # delete project
	path('vlog/',views.vlog), # used for vedio vlog 
	
]


