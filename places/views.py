from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404
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
    return JsonResponse(place_to_export)


def index(request):
    template = loader.get_template('index.html')

    places = {
        'type': 'FeatureCollection',
        'features': [],
    }
    for place in Place.objects.all():
        places['features'].append(
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
        )

    context = {
        'places': places,
    }
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
