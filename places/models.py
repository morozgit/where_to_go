from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', unique=True)
    short_description = models.TextField(verbose_name='Описание', blank=True)
    long_description = HTMLField(verbose_name='Подробное описание', blank=True)
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self) -> str:
        return self.title

    class Meta:
        unique_together = ('longitude', 'latitude')


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    position = models.PositiveIntegerField(
        default=0,
        blank=True,
        verbose_name='Позиция изображения',
        db_index=True
    )
    place = models.ForeignKey(Place,
                              related_name='images',
                              verbose_name='Место',
                              on_delete=models.CASCADE
                              )

    class Meta:
        ordering = ['position']