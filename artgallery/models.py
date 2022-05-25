from django.db import models

class Images(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    image_name = models.CharField(max_length=30)
    image_description = models.TextField(blank=True)
    
    
class ImageLocation(models.Model):
    location = models.CharField(max_length=60)
    
class ImageCategory(models.Model):
    category = models.CharField(max_length=60)
