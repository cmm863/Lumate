# Create your views here.
from django.shortcuts import render_to_response
from guestbook.models import Guest
from django.http import HttpResponse
from form import GuestForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


def guests(request):
    return render_to_response('guests.html',
                             {'guests': Guest.objects.all() })

def guest(request, guest_id=1):
    return render_to_response('guest.html',
                             {'guest': Guest.objects.get(id=guest_id) })

def create(request):
    if request.POST:
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/guestbook/all')
    else: 
        form = GuestForm()
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = form

    return render_to_response('create_guest.html', args)
