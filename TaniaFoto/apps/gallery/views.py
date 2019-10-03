from django.shortcuts import render
from .models import *

def portrait(request):
    portraits_detail_list = Gallery_Portrait.objects.get()
    return render(request, 'gallery/portrait.html', {'portraits_detail_list': portraits_detail_list})

def family(request):
    family_detail_list = Gallery_Famyly.objects.get()
    return render(request, 'gallery/family.html', {'family_detail_list': family_detail_list})

def wedding(request):
    wedding_detail_list = Gallery_Weding.objects.get()
    return render(request, 'gallery/wedding.html', {'wedding_detail_list': wedding_detail_list})
