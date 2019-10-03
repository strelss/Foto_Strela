from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    path('portrait/', views.portrait, name = 'portrait'),
    path('family/', views.family, name = 'family'),
    path('wedding/', views.wedding, name='wedding')
]