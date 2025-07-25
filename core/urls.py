from django.urls import path
from .views import *

urlpatterns = [
    path('', landing_page, name='home'),
    path('mars/', mars_photos, name='mars_photos'),
    path('iss-tracker/',iss_tracker, name='iss_tracker'),
    path('satellite-constellation/', satellite_constellation_view, name='satellite_constellation'),
    # path('api/satellites/',fetch_satellites_by_group, name='fetch_satellites_by_group'),
]