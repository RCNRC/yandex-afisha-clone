from django.db import models


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
        max_length=201
    )
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return f"{self.title}"


class Image(models.Model):
    special_id = models.IntegerField(
        null=True,
        blank=True,
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="images"
    )
    content = models.ImageField(
        upload_to=None,
        height_field=None,
        width_field=None,
        max_length=210,
    )

    def __str__(self):
        return f"{self.special_id} {self.place.title}"
