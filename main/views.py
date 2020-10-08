from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    user  = User.objects.all()
    skills = Skills.objects.all()
    projects = Projects.objects.all()
    experience = Experience.objects.all()
    languages = Languages.objects.all()
    context = {
        'user': user,
        'skills': skills,
        'projects': projects,
        'experience': experience,
        'languages': languages

    }
    return render(request, 'main/index.html', context)
