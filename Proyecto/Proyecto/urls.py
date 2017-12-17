#from django.conf.urls import patterns, include, url
#from django.contrib import admin
#from django.urls import path
#from pokemon.views import *


#urlpatterns = [
    # Examples:
    # url(r'^$', 'Proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^admin/', include(admin.site.urls)),
  #  url(r'^$', views.index, name='index'),
    #url('', Index.as_view(), name='index'),
    #url('', Index.as_view(), name='index'),

#]

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pokemon/', include('pokemon.urls')),
]
