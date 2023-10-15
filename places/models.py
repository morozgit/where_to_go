from django.db import models
from tinymce.models import HTMLField



class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(verbose_name='Описание')
    description_long = HTMLField(verbose_name='Подробное описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self) -> str:
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    position = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    place = models.ForeignKey(Place,
                              related_name='images',
                              verbose_name='Место',
                              on_delete=models.CASCADE
                              )

    class Meta:
        ordering = ['position']