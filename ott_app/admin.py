from django.contrib import admin

# Register your models here.


# custom code start
#--------------------------------------------
from ott_app.models import ott_app # ott_app(dir).models(py) > ott_app(class)


class ott_app_admin(admin.ModelAdmin): # child class name optinol & admin.ModelAdmin >> admin.py > ModelAdmin is parent class
    
    # (these all are optinol) [admin dashboard presentation purpose]
    list_display = ( 'movie_name', 'movie_release_date','movie_language','movie_actors', 'is_publish', 'created_at')
    list_display_links = ('movie_name',)
    list_filter = ('movie_release_date','created_at',)
    list_editable = ('is_publish',)
    search_fields = ('movie_name', 'movie_language')
    ordering = ('movie_release_date',) 
    #exclude = ('movie_description',)


admin.site.register(ott_app,ott_app_admin) # here ott_app (models.py > class), [optinol : ott_app_admin (.py [thispage] >> class )]

#---------------------------------------------
# custom code end


