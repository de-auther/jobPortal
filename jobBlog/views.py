from django.shortcuts import render
from .models import blog_db

# Create your views here.


def job_blog(request):

    blogs = blog_db.objects.all()

    return render(request,'jobBlog/blog_list.html', {'blogs':blogs})


def blog_details(request,slug):
    blogs = blog_db.objects.filter(slug=slug)
    return render(request, 'jobBlog/blog_details.html', {'blogs':blogs})