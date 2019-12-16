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
