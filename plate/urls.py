from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^(?P<round_no>[0-9]+)/$', views.detail, name='detail'),
    url(r'register$',views.register, name='register'),
]
