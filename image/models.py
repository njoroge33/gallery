from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)

class Location(models.Model):
    location_name = models.CharField(max_length=30)

class Images(models.Model):
    your_image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=250)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images
