from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # /usuario/2/
    url(r'^(?P<usuario_id>[0-9]+)/$', views.detalles, name='detalles'),
]