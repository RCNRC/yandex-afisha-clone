from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from places.models import Place


def get_place(request, place_id):
    place_record = get_object_or_404(Place, id=place_id)
    place = {
        'title': place_record.title,
        'imgs': [image.content.url for image in place_record.images.all()],
        'description_short': place_record.description_short,
        'description_long': place_record.description_long,
        'coordinates': {
            'lat': place_record.lat,
            'lng': place_record.lng,
        },
    }
    dumps_params = {
        'ensure_ascii': False,
        'indent': 2,
    }
    return JsonResponse(
        place,
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
