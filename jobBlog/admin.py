from django.contrib import admin
from .models import blog_db

# Register your models here.
class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['head']}
admin.site.register(blog_db,blogAdmin)