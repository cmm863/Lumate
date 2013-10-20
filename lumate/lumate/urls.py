from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lumate.views.index'),
    # url(r'^lumate/', include('lumate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^guestbook/', include('guestbook.urls')),
    # Uncomment the next line to enable the admin:
    #  url(r'^admin/', include(admin.site.urls)),
)

