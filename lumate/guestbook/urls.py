from django.conf.urls import patterns, url

from guestbook import views

urlpatterns = patterns('',
    url(r'^all/$', 'guestbook.views.guests'),
    url(r'^get/(?P<guest_id>\d+)/$', 'guestbook.views.guest'),
    url(r'^create/$', 'guestbook.views.create'),
)

