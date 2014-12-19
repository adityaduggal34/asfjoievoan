from django.shortcuts import render

def home(request):
	"Site homepage"
	data={}
	template='mainsite/home.html'
	return render(request,template,data)
