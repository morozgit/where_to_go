import os
from io import BytesIO

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from PIL import Image

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = 'Загрузка данных из json'

    def add_arguments(self, parser):
        parser.add_argument('data_url', type=str, help='Введите ссылку на данные')

    def handle(self, *args, **kwargs):
        url = kwargs['data_url']
        response = requests.get(url)
        response.raise_for_status()
        answer = response.json()

        title = answer['title']
        images_url = answer['imgs']
        short_description = answer['description_short']
        long_description = answer['description_long']
        longitude = answer['coordinates']['lng']
        latitude = answer['coordinates']['lat']

        place, created = Place.objects.get_or_create(
            title=title,
            longitude=longitude,
            latitude=latitude,
            defaults={
                'short_description': short_description,
                'long_description': long_description,
            }
        )
        for image_url in images_url:
            response = requests.get(image_url)
            response.raise_for_status()
            image_name = os.path.basename(image_url)
            PlaceImage.objects.create(
                place=place,
                image=ContentFile(response.content, name=image_name)
            )
            # image_bin = Image.open(BytesIO(response.content))
            # image_bytes_io = BytesIO()
            # image_bin.save(image_bytes_io, format='JPEG')
            # image_bytes = image_bytes_io.getvalue()
            # content = ContentFile(image_bytes)
            # place_image = PlaceImage()
            # place_image.place_id = place.id
            # place_image.image.save(f'{title}{image_num}.jpg', content, save=True)