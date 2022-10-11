from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Rating_field(models.Model):
    accuracy=models.CharField(max_length = 200,null=True,blank=True)
    checkIn=models.CharField(max_length = 200,null=True,blank=True)
    cleanliness=models.CharField(max_length = 200,null=True,blank=True)
    communication=models.CharField(max_length = 200,null=True,blank=True)
    location=models.CharField(max_length = 200,null=True,blank=True)
 

class ScrapedData(models.Model):
    listing_id = models.CharField(max_length = 200,null=True,blank=True)
    name_of_listing =models.CharField(max_length = 200,null=True,blank=True)
    city=models.CharField(max_length = 200,null=True,blank=True)
    state=models.CharField(max_length = 200,null=True,blank=True)
    country=models.CharField(max_length = 200,null=True,blank=True)
    bedrooms=models.CharField(max_length = 200,null=True,blank=True)
    bathrooms=models.CharField(max_length = 200,null=True,blank=True)
    beds=models.CharField(max_length = 200,null=True,blank=True)
    accomodation_total=models.CharField(max_length = 200,null=True,blank=True)
    listing_amenmodels= models.CharField(max_length = 200,null=True,blank=True)
    host_name=models.CharField(max_length = 200,null=True,blank=True)
    host_id=models.CharField(max_length = 200,null=True,blank=True)
    latitude=models.CharField(max_length = 200,null=True,blank=True)
    longitude=models.CharField(max_length = 200,null=True,blank=True)
    room_type=models.CharField(max_length = 200,null=True,blank=True)
    picture_url =models.CharField(max_length = 200,null=True,blank=True)
    ratings = models.ForeignKey(Rating_field,on_delete=models.CASCADE,null=True,blank=True)