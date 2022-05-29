from email.mime import image
from django.db import models

class ImageLocation(models.Model):
    location = models.CharField(max_length=60)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
        
    @classmethod
    def update_location(cls, id, location):
        '''
        Function that enables to update location
        '''
        cls.objects.filter(id=id).update(location=location)
    
class ImageCategory(models.Model):
    category = models.CharField(max_length=60)
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
        
    @classmethod
    def update_category(cls,id,category):
        cls.objects.filter(id=id).update(category=category)
    
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
    def get_image_by_id(cls,id):
        images = cls.objects.get(id=id)
        return images
    @classmethod
    def search_image(cls, search_category):
        images_by_category = cls.objects.filter(image_category__category__icontains=search_category)
        return images_by_category
    
    @classmethod
    def filter_by_location(cls,location):
        image_by_location = cls.objects.filter(image_location__location = location)
        return image_by_location
    
    
    def delete_image(self):
        self.delete()
    
    def save_image(self):
        self.save()
        
    @classmethod
    def image_update(cls, id, value):
        '''
        Function to enable admin update images
        '''
        image = cls.objects.filter(id=id).update(image=value)
        return image
        
    class Meta:
        ordering = ['image_location']
    
    
