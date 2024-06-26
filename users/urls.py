from django.urls import path
from .views import SignupView, LoginView,DashboardView, LogoutView
urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('logout/', LogoutView.as_view(), name="logout")  
]
