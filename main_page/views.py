from django.http import HttpResponse
from django.template import loader
from places.models import Place

def get_places():
    places = {
        "type": "FeatureCollection",
        "features": [],
    }

    places_contents = Place.objects.all()
    for place in places_contents:
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
                    "detailsUrl": place.details_url,
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
