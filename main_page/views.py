from django.http import HttpResponse
from django.template import loader

def get_places():
    places = {
        "type": "FeatureCollection",
        "features": [],
    }
    places["features"].append(
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": "static/places/moscow_legends.json"
          }
        }
    )
    places["features"].append(
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": "static/places/roofs24.json"
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
