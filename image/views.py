from django.shortcuts import render
from .models import Images

# Create your views here.
def index(request):
    images=Images.get_images()
    return render(request, 'index.html', {'images':images})
