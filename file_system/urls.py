from django.urls import path
from file_system import views

urlpatterns = [
    path(r'^files/$', views.show_files_system),
]