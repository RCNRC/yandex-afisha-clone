from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from places.models import Place


def get_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_to_export = {
        'title': place.title,
        'imgs': [image.content.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        },
    }
    dumps_params = {
        'ensure_ascii': False,
        'indent': 2,
    }
    return JsonResponse(
        place_to_export,
        safe=False,
        json_dumps_params=dumps_params,
    )


def index(request):
    places = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.title,
                    'detailsUrl': reverse(get_place, args=[place.id])
                }
            }
            for place in Place.objects.all()
        ],
    }

    context = {
        'places': places,
    }
    return render(request, 'index.html', context=context)
