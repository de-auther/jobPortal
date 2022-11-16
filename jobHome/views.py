
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.db.models import Q
from jobBlog.models import blog_db
from .models import categories_db, feedBack_db, job_list_db, social_media_db
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse

# Create your views here.

def job_home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        db = feedBack_db(name=name, email=email, message=message)
        db.save()
        categories = categories_db.objects.all()
        jobs = job_list_db.objects.all()
        blogs = blog_db.objects.all()
        links = social_media_db.objects.all()
    else:
        blogs = blog_db.objects.all()
        categories = categories_db.objects.all()
        jobs = job_list_db.objects.all()
        links = social_media_db.objects.all()
    return render(request, 'jobHome/index.html', {'categories':categories, 'jobs':jobs, 'blogs':blogs, 'links':links})
    


    




def job_list(request,c_slug=None):
    if c_slug != None:
        categories = categories_db.objects.all()
        pk = get_object_or_404(categories_db,slug=c_slug)
        jobs = job_list_db.objects.filter(category=pk)
        
    else:
        categories = categories_db.objects.all()
        jobs = job_list_db.objects.all()
    return render(request,'jobHome/job_list.html',{'jobs':jobs, 'categories': categories})



def job_details(request,c_slug, j_slug):
    pk = get_object_or_404(categories_db, slug=c_slug)
    jobs = job_list_db.objects.filter(category = pk)
    details = job_list_db.objects.get(category__slug=c_slug, slug=j_slug)
    v = details.vaccancy_details
    print(v)
    return render(request,'jobHome/job_details.html' , {'details':details,'jobs':jobs})






def search(request):
    if 'address' in request.GET:
        key = request.GET['address']
        jobs = job_list_db.objects.filter(Q(post_name__contains=key)|Q(organization_name__contains=key))
        return render(request,'jobHome/job_list.html',{'jobs':jobs,})

       
        

    

    

def contact(request):
    return render(request,'jobHome/contact.html')