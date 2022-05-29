from email.mime import image
from django.db import models


class ImageLocation(models.Model):
    location = models.CharField(max_length=60)
    
    def save_location(self):
        self.save();
    
class ImageCategory(models.Model):
    category = models.CharField(max_length=60)
    
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(category__icontains=search_term)
        return news
    
class Images(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    image_name = models.CharField(max_length=30)
    image_description = models.TextField(blank=True)
    image_location = models.ForeignKey(ImageLocation,on_delete=models.CASCADE,default=0)
    image_category = models.ForeignKey(ImageCategory,on_delete=models.CASCADE,default=0)
    
    
    @classmethod
    def all_images(cls):
        image = cls.objects.all()
        return image
    
    def get_image_by_id(cls):
        images = cls.objects.get(id)
        return images
    @classmethod
    def search_image(cls,category):
        image_by_category = cls.objects.filter(image_category__icontains = category)
        return image_by_category
    
    @classmethod
    def filter_by_location(cls,location):
        image_by_location = cls.objects.filter(image_location = location)
        return image_by_location
    
    def save_image(self):
        self.save()
        
    class Meta:
        ordering = ['image_location']
    
    
