from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)

class Location(models.Model):
    location_name = models.CharField(max_length=30)

