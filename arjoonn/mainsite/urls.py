from django.conf.urls import patterns,url

urlpatterns=patterns('mainsite.views',
	url(r'^$','home',name='home'),

)
