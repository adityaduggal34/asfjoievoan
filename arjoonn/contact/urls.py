from django.conf.urls import patterns,url
from contact import views
urlpatterns=patterns('',
	url('^$',views.home,name='home'),
	url('^success/$',views.success,name='success'),
	url('^fail/$',views.fail,name='fail'),
)
