from django.shortcuts import render
from .models import Images, Location

# Create your views here.
def index(request):
    images=Images.get_images()
    locations = Location.get_locations()
    return render(request, 'index.html', {'images':images, "locations":locations})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        searched_term = request.GET.get("category")
        searched_pictures = Images.search_by_category(searched_term)
        message = f"{searched_term}"

        return render(request, 'search.html', {"message": message, "pics": searched_pictures})

    else:
        message = "You have not searched for any picture"
        return render(request, 'search.html', {"message": message})
