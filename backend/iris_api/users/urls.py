from django.conf.urls import  include, url
from django.views.generic import TemplateView
from . import views




urlpatterns=[
	url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout'),
]