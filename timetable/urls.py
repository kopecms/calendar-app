from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_day/$', views.get_day, name='get_day'),
    url(r'^create_task/$', views.create_task, name = "create_task"),
    url(r'^$', views.index, name = 'index'),
]
