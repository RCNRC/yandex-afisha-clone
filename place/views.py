from django.shortcuts import render
from places.models import Place
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def get_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_to_export = {
        "title": place.title,
        "imgs": [image.content.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng,
        },
    }
    return JsonResponse(place_to_export)
