from django.contrib import admin
from .models import Images,ImageLocation,ImageCategory

admin.site.register(Images)
admin.site.register(ImageLocation)
admin.site.register(ImageCategory)

# Register your models here.
