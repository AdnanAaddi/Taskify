from django.urls import path
from projects.views import CreateProjectView, UpdateProjectView
urlpatterns = [
    path('createproject/', CreateProjectView.as_view(), name="createproject"),
    path('updateproject/<int:project_id>/update/', UpdateProjectView.as_view(), name='updateproject'),
]
