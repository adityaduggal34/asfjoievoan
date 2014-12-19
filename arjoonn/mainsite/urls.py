from django.conf.urls import patterns,url

urlpatterns=patterns('mainsite.views',
	url(r'^$','home',name='home'),
	url(r'^about/$','about',name='about'),
	url(r'^workflow/$','workflow',name='workflow'),
	url(r'^team/$','team',name='team'),
	url(r'^track/$','track',name='track'),
)
