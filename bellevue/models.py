from django.db import models
from django.contrib import admin

class contacts(models.Model):
        name =  models.CharField("Contact's Name",max_length=50)
        email= models.EmailField()
        phone_number= models.CharField("Phone number",max_length =50)
        message  = models.TextField()
        date_created      = models.DateTimeField(auto_now_add= True)
        date_updated    = models.DateTimeField (auto_now =True,blank =True, null = True)


        def __unicode__ (self):
		return '%s' %(self.name)

	class Meta:
		verbose_name="Contact"
		verbose_name_plural="Contacts"


class about_us(models.Model):
        title            = models.CharField(max_length = 30)
        content 	= models.TextField()
        date_created    = models.DateTimeField(auto_now_add= True)
        date_updated    = models.DateTimeField (auto_now =True,blank =True, null = True)
        
	def __unicode__ (self):
		return '%s %s' %(self.title,self.content[:15])

	class Meta:
		verbose_name="About Us"
		verbose_name_plural="About Us"

class contact_Admin(admin.ModelAdmin):
	list_display = ('name','email','phone_number','message')
	list_filter = ('date_created','date_updated')
	search_fields = ['name']

class aboutUs_Admin(admin.ModelAdmin):
	list_display = ('title','content','date_created','date_updated')
	list_filter = ('date_created','date_updated')
	search_fields = ['content']


admin.site.register(contacts,contact_Admin)
admin.site.register(about_us,aboutUs_Admin)
