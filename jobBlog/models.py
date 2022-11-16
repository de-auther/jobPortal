from email.policy import default
from django.db import models
from django.urls import reverse

# Create your models here.

class blog_db(models.Model):
    head = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    date = models.DateField(null=True)
    
    content_brief = models.TextField(blank=True, default='')
    hd1 = models.CharField(max_length=200, blank=True, default='')
    content1 = models.TextField(blank=True, default='')
    photo1 = models.URLField(max_length=1000, blank=True, default='')
    hd2 = models.CharField(max_length=200, blank=True, default='')
    content2 = models.TextField(blank=True, default='')
    photo2 = models.URLField(max_length=1000, blank=True, default='')
    hd3 = models.CharField(max_length=200, blank=True, default='')
    content3 = models.TextField(blank=True, default='')
    photo3 = models.URLField(max_length=1000, blank=True, default='')
    hd4 = models.CharField(max_length=200, blank=True, default='')
    content4 = models.TextField(blank=True, default='')
    photo4 = models.URLField(max_length=1000, blank=True, default='')
    hd5 = models.CharField(max_length=200, blank=True, default='')
    content5 = models.TextField(blank=True, default='')
    photo5 = models.URLField(max_length=1000, blank=True, default='')
    hd6 = models.CharField(max_length=200, blank=True, default='')
    content6 = models.TextField(blank=True, default='')
    photo6 = models.URLField(max_length=1000, blank=True, default='')
    hd7 = models.CharField(max_length=200, blank=True, default='')
    content7 = models.TextField(blank=True, default='')
    photo7 = models.URLField(max_length=1000, blank=True, default='')
    hd8 = models.CharField(max_length=200, blank=True, default='')
    content8 = models.TextField(blank=True, default='')
    photo8 = models.URLField(max_length=1000, blank=True, default='')
    hd9 = models.CharField(max_length=200, blank=True, default='')
    content9 = models.TextField(blank=True, default='')
    photo9 = models.URLField(max_length=1000, blank=True, default='')
    hd10 = models.CharField(max_length=200, blank=True, default='')
    content10 = models.TextField(blank=True, default='')
    photo10 = models.URLField(max_length=1000, blank=True, default='')
    hd11 = models.CharField(max_length=200, blank=True, default='')
    content11 = models.TextField(blank=True, default='')
    photo11 = models.URLField(max_length=1000, blank=True, default='')
    hd12 = models.CharField(max_length=200, blank=True, default='')
    content12 = models.TextField(blank=True, default='')
    photo12 = models.URLField(max_length=1000, blank=True, default='')
    hd13 = models.CharField(max_length=200, blank=True, default='')
    content13 = models.TextField(blank=True, default='')
    photo13 = models.URLField(max_length=1000, blank=True, default='')
    hd14 = models.CharField(max_length=200, blank=True, default='')
    content14 = models.TextField(blank=True, default='')
    photo14 = models.URLField(max_length=1000, blank=True, default='')
    hd15 = models.CharField(max_length=200, blank=True, default='')
    content15 = models.TextField(blank=True, default='')
    photo15 = models.URLField(max_length=1000, blank=True, default='')




    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.head

    def get_url(self):
        return reverse('blog_details', args=[self.slug])









