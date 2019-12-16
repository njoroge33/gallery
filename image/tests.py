from django.test import TestCase
from .models import Images, Category, Location

# Create your tests here.
class ImagesTestClass(TestCase):

    def setUp(self):
        self.image = Images(image_name = 'meat', image_description = 'tasty beef', category = 'food', location = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Images))

    def test_save_images(self):
        self.image.save_images()
        images = Images.objects.all()
        self.asserTrue(len(images)>0)

    def test_delete_images(self):
        self.image.delete_images()
        images = Images.objects.all()
        self.asserTrue(len(images) == 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name='food')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)


class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 1)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)
