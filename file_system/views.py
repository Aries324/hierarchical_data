from django.shortcuts import render
from file_system.models import File_System
# Create your views here.
def show_files_system(request):
    return render(request, 'files.html', {'files': File_System.objects.all()})

# def index(request):
#     html = 'index.html'
#     data = File.objects.all()
#     return render(request, html, {'data': data})