from django.db import models

class variable(models.Model):
	"Control variables for various applications in the project"
	def __unicode__(self):
		return str(self.name)
	appname=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
	value=models.CharField(max_length=100,blank=True)
	file_attached=models.FileField(upload_to='control/files',blank=True,null=True,default=None)
