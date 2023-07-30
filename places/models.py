from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    type = models.CharField(
        null=True,
        max_length=100,
    )
    geometry_type = models.CharField(
        null=True,
        max_length=100,
    )
    map_title = models.CharField(
        null=True,
        max_length=100,
    )
    place_id = models.CharField(
        null=True,
        max_length=100,
    )
    details_url = models.TextField(
        null=True,
    )
    title = models.CharField(
        unique=True,
        max_length=201
    )
    description_short = models.TextField()
    description_long = HTMLField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return f"{self.title}"


class Image(models.Model):
    special_id = models.PositiveIntegerField(
        default=0,
        null=False,
        blank=False,
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="images"
    )
    content = models.ImageField(
        upload_to="./images",
        height_field=None,
        width_field=None,
        max_length=210,
    )

    class Meta:
        ordering = ['special_id']

    def __str__(self):
        return f"{self.special_id} {self.place.title}"

