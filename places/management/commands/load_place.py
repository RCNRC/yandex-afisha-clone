import json
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Importing remote json files in Place model'

    def import_image(self, image_url: str, self_place: Place):
        response = requests.get(image_url)
        response.raise_for_status()
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
            place_raw = response.json()
            if 'error' in place_raw:
                raise requests.exceptions.HTTPError(place_raw['error'])
            place, created = Place.objects.get_or_create(
                title=place_raw['title'],
                defaults={
                    'description_short': place_raw.get(
                        'description_short', ''
                    ),
                    'description_long': place_raw.get(
                        'description_long', ''
                    ),
                    'lng': place_raw['coordinates']['lng'],
                    'lat': place_raw['coordinates']['lat'],
                },
            )
            if not created:
                self.stdout.write('Creation model failure')
                return
            if 'imgs' not in place_raw or not place_raw['imgs']:
                place.images.set([])
                place.save()
            for image_url in place_raw.get('imgs', []):
                self.import_image(image_url, place)
        except requests.HTTPError as error:
            self.stdout.write(f'Request failed: {error.response.text}')
            return
        except (ValueError, json.decoder.JSONDecodeError):
            self.stdout.write('You are trying download not a json')
            return
