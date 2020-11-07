from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$', views.log_in, name= 'index'),
  url(r'^login/$', views.log_in, name= 'log_in'),
  url(r'^logout/$', views.log_out, name= 'log_out'),
  url(r'^home/$', views.home, name= 'home'),
  url(r'^signup/$', views.signup, name='signup'),
  url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
  path('profile/<slug:username>/', views.view_profile, name='view_profile'),
  # TEST
  url(r'sendsms/$', views.send_sms, name= 'sendsms'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)