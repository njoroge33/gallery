from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path(r'^search/', views.search_results,name='search_results'),
    re_path(r'^location/(?P<location>\w+)', views.location_images, name='location')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
