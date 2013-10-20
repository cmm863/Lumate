# Create your views here.
from django.shortcuts import render_to_response
from guestbook.models import Guest
from django.http import HttpResponse
from form import GuestForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import datetime


def guests(request):
    return render_to_response('guests.html',
                              {'guests': Guest.objects.all()})


def guest(request, guest_id=1):
    return render_to_response('guest.html',
                              {'guest': Guest.objects.get(id=guest_id)})


def create(request):
    if request.POST:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            i_add = x_forwarded_for.split(',')[0]
        else:
            i_add = request.META.get('REMOTE_ADDR')
        brows_info = request.META.get('HTTP_USER_AGENT', 'unknown')
        today = datetime.date.today()
        formf = GuestForm(request.POST)
        form = formf.save(commit=False)
        form.ip_address = i_add
        form.browser_info = brows_info
        form.date_signed = today
        form.save()

        return HttpResponseRedirect('/guestbook/all')
    else:
        form = GuestForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('create_guest.html', args)

