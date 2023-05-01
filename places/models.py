from django.db import models


class Place(models.Model):
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
