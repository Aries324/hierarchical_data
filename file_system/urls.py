from django.urls import path
from file_system import views

urlpatterns = [
    path('', views.show_files_system, name='homepage'),
    path('addfiles/', views.add_files_view)
]