from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^register/$', views.register, name= 'register'),
  url(r'^login/$', views.log_in, name= 'log_in'),
  url(r'^logout/$', views.log_out, name= 'log_out'),
  url(r'^home/$', views.home, name= 'home'),
]
