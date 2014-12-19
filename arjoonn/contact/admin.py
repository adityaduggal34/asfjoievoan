from django.contrib import admin
import contact

class MessageAdmin(admin.ModelAdmin):
	list_display=['name','email','message','stamp']
	list_filter=['read']
	search_fields=['name','message']
admin.site.register(contact.models.message,MessageAdmin)
