"""SE_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index, name="index"),
    # path('', views.HomeView.as_view(), name='home'),
    # path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    # #pk is a primary key for every blog entry
    path('', include('THG.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='THG/templates/password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="THG/templates/password_reset/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='THG/templates/password_reset/password_reset_complete.html'), name='password_reset_complete'),   

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
admin.site.site_header = "TechHackGyan Admin"
admin.site.site_title = "TechHackGyan Admin Panel"
admin.site.index_title = "Welcome to TechHackGyan Admin Panel"