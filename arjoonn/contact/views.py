from django.shortcuts import render,redirect
import control,contact
def home(request):
	"homepage of contact form"
	data={}
	template='contact/home.html'
	if request.method=='GET':
		data['form']=contact.models.MessageForm()
	if request.method=='POST':
		try:
			form=contact.models.MessageForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('contact:success')
			else:
				data['form']=form
		except Exception as e:
			print e
			return redirect('contact:fail')
	return render(request,template,data)
def success(request):
	"Successfully submitted form"
	data={}
	template='contact/success.html'
	return render(request,template,data)
def fail(request):
	"Failed in the  submitted form"
	data={}
	template='contact/fail.html'
	data['message']=control.models.variable.objects.filter(appname='contact',name='away_message')
	return render(request,template,data)
