"""jobPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from operator import concat
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import settings
from jobHome import views as views_home
from jobBlog import views as views_blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_home.job_home, name='job_home'),
    path('job_list_all/', views_home.job_list, name='job_list'),
    path('job_list_all/<slug:c_slug>/', views_home.job_list, name='job_list'),
    path('contact/', views_home.contact, name='contact'),
    path('job_list_all/<slug:c_slug>/<slug:j_slug>/',views_home.job_details, name= 'job_details'),
    path('blog_list/', views_blog.job_blog, name='job_blog'),
    path('blog_list/<slug:slug>/', views_blog.blog_details, name='blog_details'),
    path('search_result/',views_home.search, name='search')
    

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


