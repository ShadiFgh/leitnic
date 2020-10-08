from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.log_in, name= 'index'),
  url(r'^login/$', views.log_in, name= 'log_in'),
  url(r'^logout/$', views.log_out, name= 'log_out'),
  url(r'^home/$', views.home, name= 'home'),
  url(r'^signup/$', views.signup, name='signup'),
  # TEST
  url(r'sendsms/$', views.send_sms, name= 'sendsms'),
]
