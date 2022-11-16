from django.contrib import admin

from jobHome.models import categories_db, feedBack_db, job_list_db, social_media_db

# Register your models here.
class categories_db_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['categories']}

admin.site.register(categories_db, categories_db_admin)


class job_list_db_admin(admin.ModelAdmin):
    prepopulated_fields =  {'slug':('post_name',)}

admin.site.register(job_list_db, job_list_db_admin)

admin.site.register(feedBack_db)
admin.site.register(social_media_db)


