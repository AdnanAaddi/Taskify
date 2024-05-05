from typing import Any
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import ProjectUser
from projects.models import Project
from django.views.generic import TemplateView, ListView, DetailView
from projects.views import display_projects

class SignupView(View):
    def get(self, request):
        return render(request, 'users/signup.html')

    def post(self, request):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        profile_picture = request.FILES.get('profile_picture', None)

        if name and email and password1 and password2:
            if ProjectUser.objects.filter(email=email).exists():
                print("User Already Exists")
                return render(request, 'users/signup.html')
            
            user = ProjectUser.objects.create_user(name, email, password1)
            user.name = name
            if profile_picture:
                user.profile_picture = profile_picture
            
            user.save()
            print('User created:', user)

            return redirect('/login/')
        else:
            print('Something went wrong')
            return render(request, 'users/signup.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = ''
        try:
            username = ProjectUser.objects.get(email=email).username
        except ProjectUser.DoesNotExist:
            return HttpResponse('invalid_login')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Logged in")
            return redirect('dashboard')
        else:
            print("Not logged in")
            return redirect('signup')
        
class DashboardView(LoginRequiredMixin, TemplateView):
    print("Dashboard Called")
    login_url = '/login/'
    template_name = 'users/dashboard.html'

    def get_context_data(self, **kwargs):
        print("Context Method Called ")
        context= super().get_context_data(**kwargs)
        user_projects = display_projects(self.request.user)
        print(self.request.user)
        context['user_projects'] = user_projects
        return context

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    
