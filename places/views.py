from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from places.models import Place
from place.views import get_place


def get_places():
    places = {
        "type": "FeatureCollection",
        "features": [],
    }

    for place in Place.objects.all():
        places["features"].append(
            {
                "type": place.type,
                "geometry": {
                    "type": place.geometry_type,
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.map_title,
                    "placeId": place.place_id,
                    "detailsUrl": reverse(get_place, args=[place.id])
                }
            }
        )
        
    return places

def index(request):
    template = loader.get_template('index.html')
    context = {
        "places": get_places()
    }
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
