from datetime import timezone
from email import message
from email.policy import default
from django.urls import reverse
from django.db import models
# Create your models here.



class categories_db(models.Model):
    categories = models.CharField(max_length=50, unique = True)
    photo = models.URLField(blank=True, max_length=500, default='')
    slug = models.SlugField(max_length=50, unique= True)

    class Meta:
        ordering = ['-categories']

    def __str__(self):
        return self.categories
    
    def get_url(self):
        return reverse('job_list', args=[self.slug])
    


class job_list_db(models.Model):
    organization_name = models.CharField(max_length=200, blank=True, default='')
    photo = models.URLField(max_length=1000, blank=True, default='')
    post_name = models.CharField(max_length=200, blank=True, default='')
    slug = models.SlugField(max_length=200, unique = True )
    job_type = models.CharField(max_length=100,blank=True, default='')
    recruitement_type = models.CharField(max_length=100, blank=True, default='')
    advt_nbr = models.CharField(max_length=100, blank=True, default='')
    vaccancies = models.IntegerField(blank=True, default='')
    job_location = models.CharField(max_length=100, blank=True, default='')
    salary = models.TextField(blank=True, default='')
    mod_of_application = models.CharField(max_length=100, blank=True, default='')
    start_date = models.DateField(null=True, blank=True, default='')
    end_date = models.DateField(null=True, blank=True, default='')
    category = models.ForeignKey(categories_db, on_delete = models.CASCADE)
    dates_details = models.TextField(null=True, blank=True, default='')
    vaccancy_details = models.TextField(blank=True, default='')
    salary_details = models.TextField(blank=True, default='')
    age_limit_details = models.TextField(blank=True, default='')
    qualification_details = models.TextField(blank=True, default='')
    application_fee_details = models.TextField(blank=True, default='')
    selection_process_details = models.TextField(blank=True, default='')
    how_to_apply = models.TextField(blank=True, default='')
    apply_link = models.URLField(blank=True, max_length = 1000, default='')
    
    
    class Meta:
        ordering = ['-end_date']


    def __str__(self):
        return self.post_name

    def get_url(self):
        return reverse('job_details', args=[self.category.slug, self.slug])




class feedBack_db(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


    class Meta:
        ordering = ['-name']


    def __str__(self) -> str:
        return super().__str__()



class social_media_db(models.Model):
    whatsapp = models.URLField(max_length=1000, blank=True)
    telegram = models.URLField(max_length=1000, blank=True)


    