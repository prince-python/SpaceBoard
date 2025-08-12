
# Create your views here
from django.shortcuts import render

def landing_page(request):
    return render(request, 'index.html')



import requests
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from datetime import datetime




API_KEY = 'wbcIjdzTOco4y7feBKfk7Tt5MYVArH6z303KcL5J'  # Replace with your own NASA API key if needed
BASE_URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'

def mars_photos(request):
    rover = request.GET.get('rover', 'perseverance')
    earth_date = request.GET.get('date', '')

    if not rover:
        return HttpResponseBadRequest("Rover not specified")

    params = {'api_key': API_KEY}
    if earth_date:
        params['earth_date'] = earth_date
    else:
        params['sol'] = 1000  # fallback default

    url = f"{BASE_URL}{rover}/photos"
    response = requests.get(url, params=params)
    data = response.json()

    photos = data.get('photos', [])
    return render(request, 'mars.html', {
        'photos': photos,
        'rover': rover,
        'earth_date': earth_date
    })




from django.shortcuts import render

def iss_tracker(request):
    return render(request, 'iss_tracker.html')




import requests
from django.http import JsonResponse
from django.shortcuts import render

def satellite_constellation_view(request):
    return render(request, 'constellation.html')

# def fetch_satellites_by_group(request):
#     group = request.GET.get('group', 'starlink')  # default to starlink
#     url = f"https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json"

#     try:
#         response = requests.get(url)
#         data = response.json()
#         return JsonResponse(data, safe=False)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)
