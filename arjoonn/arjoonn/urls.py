from django.conf.urls import patterns, include, url
from django.contrib import admin
from arjoonn import views

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^contact/',include('contact.urls',namespace='contact-urls',app_name='contact')),
)
