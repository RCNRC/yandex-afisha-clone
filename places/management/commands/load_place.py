from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
import requests
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Importing remote json files in Place model'

    def import_image(self, image_url: str, self_place: Place):
        response = requests.get(image_url)
        response.raise_for_status()
        if 'error' in response:
            raise requests.exceptions.HTTPError(response['error'])
        image_content = ContentFile(
            content=response.content,
            name=image_url.split('/')[-1]
        )
        Image.objects.create(
            place=self_place,
            content=image_content
        )

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        url = options['url']
        try:
            response = requests.get(url)
            response.raise_for_status()
            if 'error' in response:
                raise requests.exceptions.HTTPError(response['error'])
            place_import = response.json()
            place, created = Place.objects.get_or_create(
                title=place_import['title'],
                defaults={
                    'description_short': place_import['description_short']
                    if 'description_short' in place_import else '',
                    'description_long': place_import['description_long']
                    if 'description_long' in place_import else '',
                    'lng': place_import['coordinates']['lng'],
                    'lat': place_import['coordinates']['lat'],
                },
            )
            if not created:
                self.stdout.write('Creation model failure', ending='\n')
                return
        except requests.HTTPError as error:
            self.stdout.write(f'Request failed: {error.response.text}')
            return

        if 'imgs' not in place_import or not place_import['imgs']:
            place.images.set([])
            place.save()

        for image_url in place_import['imgs']:
            try:
                self.import_image(image_url, place)
            except requests.HTTPError as error:
                self.stdout.write(f'Request image failed {error.response.text}')
