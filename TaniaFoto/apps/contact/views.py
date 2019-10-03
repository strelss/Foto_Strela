from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Contact

def contact_form(request):
    return render(request, 'contact/contact_form.html')

def leave_contact(request):
    a = Contact(contact_first_name = request.POST['fname'], contact_last_name = request.POST['lname'], contact_email = request.POST['email'], contact_massage = request.POST['message'])
    a.save()
    return render(request, 'contact/leave_contact.html')
    # return HttpResponseRedirect( reverse('contact:leave_contact'))
