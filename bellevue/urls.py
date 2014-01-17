from django.conf.urls.defaults import *
from views import *


urlpatterns = patterns('',
		url(r'^$', 'bellevue.views.home'),
                url(r'^aboutUs/$', 'bellevue.views.abtus'),
                url(r'^media/$', 'bellevue.views.media'),
                url(r'^contactUs/$', 'bellevue.views.contact'),
		
                
)
