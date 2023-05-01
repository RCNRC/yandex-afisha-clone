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
