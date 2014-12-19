from django.shortcuts import render




def home(request):
	"Site homepage"
	data={}
	template='mainsite/home.html'
	return render(request,template,data)
def about(request):
	"About our work"
	data={}
	template='mainsite/about.html'
	return render(request,template,data)
def workflow(request):
	"About our work"
	data={}
	template='mainsite/workflow.html'
	return render(request,template,data)
	
def team(request):
	"About our work"
	data={}
	template='mainsite/team.html'
	return render(request,template,data)

def track(request):
	"My past and current works"
	data={}
	template="mainsite/works.html"
	return render(request,template,data)
