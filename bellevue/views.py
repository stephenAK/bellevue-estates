from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.template import Context, loader
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.loading import get_model
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import datetime
from models import *
from django import  forms 
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail




def home(request):
          date_time = datetime.datetime.now().strftime("%G")
          return render_to_response('bellevue/index.html', {'date_time':date_time,'user': request.user})

def abtus(request):
          return render_to_response('bellevue/abtUs.html', {'user': request.user})


def media(request):
          return render_to_response('bellevue/media.html', {'user': request.user})







class ContactForm(ModelForm):
	class Meta:
		model = contacts
		exclude = ['date_created','date_updated']
        	fields  = ('name','email','phone_number','message',)


@csrf_exempt
def contact(request):
          modaL  = ""
          sender = ""
          try:
    	     if request.session["modaL"] == "modal":
                sender = request.session["sender"]
		modaL = "modal"
		request.session["modaL"] = ""
                request.session["sender"] =""	
		   
          except KeyError:
	        request.session["modaL"] = ""
          form = ContactForm(request.POST)
          if request.method == 'POST':
              
               if form.is_valid():
                   form1 = contacts()
                   form1.name = form.cleaned_data["name"]
                   form1.email = form.cleaned_data["email"]
	           form1.phone_number =  form.cleaned_data["phone_number"]
                   form1.message = form.cleaned_data["message"]
                   form1.save()
                   request.session["modaL"] = "modal"
                   request.session["sender"] = form1.name
                   html_contenT = "Hello\n" + form1.message +"\nThanks.\n"+form1.name+"\n"+form1.phone_number+"\n"+form1.email
                   try:
                       send_mail('Website Contact',html_contenT,'form1.email',['blupaygh@gmail.com'],fail_silently=False)
                   except KeyError:
                       pass
	           modaL = "on"
                   return HttpResponseRedirect('/contactUs')
          return render_to_response('bellevue/contact.html', {'sender':sender,'modaL':modaL,'form':form, 'user': request.user})
