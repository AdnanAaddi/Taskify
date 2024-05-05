from django.shortcuts import render, redirect,  get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from projects.forms import ProjectForm , UpdateProjectForm
from projects.models import Project
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class CreateProjectView(LoginRequiredMixin, View):
    login_url = '/login/'  # Specify the login URL
    
    def get(self, request):
        form = ProjectForm()
        return render(request, 'projects/create_project.html', {'form': form})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            form.save_m2m()
            return redirect('dashboard')  # Redirect to the dashboard after project creation
        return render(request, 'projects/create_project.html', {'form': form})
        

def display_projects(user):
    user_projects = Project.objects.filter(owner=user)
    return user_projects
    

