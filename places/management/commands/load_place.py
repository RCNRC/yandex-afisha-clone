from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Place, Image
import requests


class Command(BaseCommand):
    help = 'Importing remote json files in Place model'

    def import_image(self, image_url: str, self_place: Place):
        response = requests.get(image_url)
        image_content = response.content
        image = Image.objects.create(
            place=self_place,
        )
        image.content.save(image_url.split("/")[-1], ContentFile(image_content), save=True)

    def add_arguments(self, parser):
        parser.add_argument('url', nargs=1, type=str)

    def handle(self, *args, **options):
        url = options['url'][0]
        if not url:
            self.stdout.write("No file founded", ending='\n')
            return
        try:
            response = requests.get(url)
            place_import = response.json()
            place, created = Place.objects.get_or_create(
                title=place_import["title"],
                description_short=place_import["description_short"],
                description_long=place_import["description_long"],
                lng=place_import["coordinates"]["lng"],
                lat=place_import["coordinates"]["lat"],
                type="Feature",
                geometry_type="Point",
                map_title=place_import["title"],
                place_id="1",
                details_url=url,
            )
            if not created:
                self.stdout.write("Creation model failure", ending='\n')
                return
        except requests.HTTPError:
            self.stdout.write("Request failed", ending='\n')
            return
        
        for image_url in place_import["imgs"]:
            try:
                self.import_image(image_url, place)
            except requests.HTTPError:
                self.stdout.write("Request image failed", ending='\n')
