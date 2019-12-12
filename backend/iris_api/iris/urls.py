from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views




urlpatterns=[
	url(r'^import_data/$', views.import_data, name='import_data'),
    url(r'', views.All.as_view()),
    url(r'<int:pk>/', views.Detail.as_view()),
]