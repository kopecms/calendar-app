from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create_post/$', views.create_post, name = "more"),
    url(r'^$', views.index, name = 'index'),
]
