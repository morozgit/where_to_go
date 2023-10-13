from django.shortcuts import render
from .models import Place
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


def show_map(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
          {
            "type": "Feature",
            "geometry": {
              "type": "Point",
              "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
              "title": place.title,
              "placeId": place.id,
              "detailsUrl": reverse('place-image', args=[place.id])
            }
          }
        )
    places_geojson = {
      "type": "FeatureCollection",
      "features": features
    }
    print(places_geojson)
    context = {'geojson': places_geojson}
    return render(request, 'index.html', context=context)


def show_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    image_path = [place_image.image.url for place_image in place.images.all()]
    place_data = {
        "title": place.title,
        "imgs": image_path,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
      }

    return JsonResponse(place_data, safe=False, json_dumps_params={'ensure_ascii': False , 'indent': 2})