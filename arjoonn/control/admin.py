from django.contrib import admin
import control

class VariableAdmin(admin.ModelAdmin):
	exclude=[]
	list_display=['name','appname','value']
	list_filter=['appname']
admin.site.register(control.models.variable,VariableAdmin)
