from django.shortcuts import render
from .models import *

def index(request):
    portraits_prev = Gallery_Portrait.objects.get()
    Famyly_prev = Gallery_Famyly.objects.get()
    Weding_prev = Gallery_Weding.objects.get()
    return render(request, 'home/index_home.html', {'portraits_prev': portraits_prev, 'Famyly_prev': Famyly_prev, 'Weding_prev': Weding_prev})

def services(request):
    return render(request, 'home/services.html')

def about(request):
    about_me_foto = About_me.objects.get()
    return render(request, 'home/about.html', {'about_me_foto': about_me_foto})
