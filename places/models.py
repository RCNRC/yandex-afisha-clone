from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        unique=True,
        max_length=201
    )
    description_short = models.TextField(
        blank=True,
    )
    description_long = HTMLField(
        blank=True,
    )
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    serial_number = models.PositiveIntegerField(
        default=0,
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images'
    )
    content = models.ImageField(
        upload_to='./images',
        height_field=None,
        width_field=None,
        max_length=210,
    )

    class Meta:
        ordering = ['serial_number']

    def __str__(self):
        return f'{self.serial_number} {self.place.title}'
