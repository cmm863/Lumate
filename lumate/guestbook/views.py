# Create your views here.
from django.shortcuts import render_to_response
from guestbook.models import Guest
from django.http import HttpResponse

def guests(request):
    return render_to_response('guests.html',
                             {'guests': Guest.objects.All() })

def guest(request, guest_id=1):
    return render_to_response('guest.html',
                             {'guest': Guest.objects.get(id=guest_id) })
