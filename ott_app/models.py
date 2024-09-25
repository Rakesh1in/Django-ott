from django.db import models
from datetime import datetime #custom ipmort

# Create your models here.


# custom code start
#-------------------------------- 
class ott_app(models.Model): # child class 'oot_app' and models(modual).Model(parentclass)) 
	movie_poster=models.ImageField(null=False, blank=False)
	movie_name=models.CharField(max_length=200,null=False,blank=False,unique=True)
	movie_release_date=models.DateField(blank=True)
	movie_language=models.CharField(max_length=20,null=False,blank=False)
	movie_director=models.CharField(max_length=100,null=False,blank=False)
	movie_actors=models.CharField(max_length=500,null=False,blank=False)
	movie_category=models.CharField(max_length=50,null=False,blank=False)
	movie_description=models.TextField(max_length=300,null=False,blank=False)
	movie_trailer_link=models.URLField(max_length=5000,null=False,blank=False)
	movie_stream_link=models.URLField(max_length=5000,null=False,blank=False)
	movie_imbd_rating=models.DecimalField(max_digits=4,decimal_places=2)
	movie_views=models.CharField(max_length=50,null=False,blank=False)
	is_publish=models.BooleanField(default=True)
	created_at=models.DateTimeField(default=datetime.now, blank=True)
	#movie_gallarys=models.ImageField()



	def __str__ (self): # for unique key presents
		return self.movie_name


#----------------------------
# custom code end