from django import forms
from django.db import models

class message(models.Model):
	"To hold a message"
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=50)
	email=models.EmailField(help_text='Where can i get back to you?')
	message=models.TextField()
	read=models.BooleanField(default=False)
	stamp=models.DateTimeField(auto_now_add=True)

#---------------FORMS---------------
class MessageForm(forms.ModelForm):
	class Meta:
		model=message
		exclude=['read','stamp']
