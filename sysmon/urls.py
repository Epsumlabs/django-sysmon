from django.urls import re_path,path, include
from django.contrib.auth import views as auth_views
from sysmon import views

urlpatterns = (
                       path('', views.index, name='index'),
                        # path('accounts/', include('django.contrib.auth.urls')),
                       re_path(r'login/$', auth_views.LoginView.as_view(template_name= 'login.html'),
                           name='login'),
                       re_path(r'logout/$', auth_views.LogoutView.as_view(template_name='logout.html'),
                           name='logout'),
                       re_path(r'info/uptime/$', views.uptime, name='uptime'),
                       re_path(r'info/memory/$', views.memusage, name='memusage'),
                       re_path(r'info/cpuusage/$', views.cpuusage, name='cpuusage'),
                       re_path(r'info/getdisk/$', views.getdisk, name='getdisk'),
                       re_path(r'info/getusers/$', views.getusers, name='getusers'),
                       re_path(r'info/getips/$', views.getips, name='getips'),
                       re_path(r'info/gettraffic/$', views.gettraffic, name='gettraffic'),
                       re_path(r'info/proc/$', views.getproc, name='getproc'),
                       re_path(r'info/getdiskio/$', views.getdiskio, name='getdiskio'),
                       re_path(r'info/loadaverage/$', views.loadaverage, name='loadaverage'),
                       re_path(r'info/platform/([\w\-\.]+)/$', views.platform, name='platform'),
                       re_path(r'info/getcpus/([\w\-\.]+)/$', views.getcpus, name='getcpus'),
                       re_path(r'info/getnetstat/$', views.getnetstat, name='getnetstat')
                       )
