"""MP_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from deshonnati_app import views,urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('abcdeadmin/', admin.site.urls),
    re_path(r'^createajinkya/$', views.create_dailyfeed, name='home'),

    re_path(r'^onepageclip/$', views.create_pageoneclip, name='pageoneclip'),
    re_path(r'^topadd/$', views.top_add, name='top_add'),
    re_path(r'^ajinkyadashboard/$', views.maindashboard, name='maindashboard'),
    re_path(r'^bottomadd/$', views.bottom_add, name='bottom_add'),
    re_path(r'^twopageclip/$', views.create_pagetwoclip, name='pagetwoclip'),
    re_path(r'^createakolaspecial/$', views.create_dailyspecialfeed, name='special'),
    re_path(r'^createbuldhanaspecial/$', views.create_dailybuldhanafeed, name='specialbuldhana'),
    re_path(r'^dash/$', views.dashboard, name='dash'),
    re_path(r'^$',views.city,name='city'),
    re_path(r'^(?P<cityid>\d+)/today/',views.dateview,name = "dailyfeed"),
    re_path(r'^(?P<cityid>\d+)/todayy/',views.mobileview,name = "mobileview"),
    re_path(r'^(?P<cityid>\d+)/backdate/',views.mobileviewform,name = "mobileviewform"),
    re_path(r'^clip/(?P<id>\d+)/',views.clipdata,name = "clip"),
    re_path(r'^akolatoday/',views.datespecialview,name = "dailyspecialfeed"),
    re_path(r'^akolatodayy/',views.datespecialmobileview,name = "datespecialmobileview"),
    re_path(r'^buldhanatoday/',views.datespecialbuldhanaview,name = "dailybuldhanafeed"),
    re_path(r'^buldhanatodayy/',views.datespecialbuldhanamobileview,name = "datespecialbuldhanamobileview"),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page= 'login'), name='logout'),
    re_path(r'^signup/$', views.signup, name='signup'),
    path('', include('deshonnati_app.urls')),
    # The direct upload functionality reports to this URL when an image is uploaded.

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
