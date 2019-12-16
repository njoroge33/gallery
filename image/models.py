from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    

class Location(models.Model):
    location_name = models.CharField(max_length=30)

    @classmethod
    def get_locations(cls):
        locations = cls.objects.all()
        return locations

class Images(models.Model):
    your_image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=250)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

    def save_images():
        self.save()

    def delete_images():
        self.delete()

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls, search_word):
        photos = cls.objects.filter(category__category_name__icontains=search_word)

        return photos

    @classmethod
    def get_by_location(cls, location):
        images = Images.objects.filter(location__location_name__icontains=location).all()

        return images


        
