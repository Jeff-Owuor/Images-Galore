from django.db import models

class Images(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length=30)
    image_description = models.TextField(blank=True)
