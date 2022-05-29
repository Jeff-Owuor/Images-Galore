from django.test import TestCase
from .models import Images,ImageCategory,ImageLocation

# Create your tests here.
class ImageLocationTestClass(TestCase):
    '''
       Test that checks the location  model
    '''
    def setUp(self):
        self.location = ImageLocation(location='Kisumu')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.location, ImageLocation))
    
    def test_savelocation(self):
        self.location.save_location()
        locations = ImageLocation.objects.all()
        self.assertTrue(len(locations) > 0)
    
class ImageCategoryTestClass(TestCase):
    '''
       Test that check the ImageCategory model
    '''
    
    def setUp(self):
        self.category = ImageCategory(category='Mashujaa')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.category, ImageCategory))
        
    def test_savecategory(self):
        self.category.save_category()
        categories = ImageCategory.objects.all()
        self.assertTrue(len(categories) > 0)
    
    
class ImageTestClass(TestCase):
    '''
      Function that checks 
    '''
    def setUp(self):
        self.location = ImageLocation(location='Kisumu')
        self.location.save_location()
        
        self.category = ImageCategory(category='Mashujaa')
        self.category.save_category()

        self.image = Images(image='media/gallery/Chess_King_Meeple_Black_Game.png',image_name='Chess king', image_description='my test',image_category=self.category,image_location=self.location)
        self.image.save_image()
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Images))
        
    def tearDown(self):
        self.location.delete_location()
        self.category.delete_category()
        self.image.delete_image()
    