# Generated by Django 4.2 on 2023-05-07 21:29

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0023_remove_place_details_url_remove_place_geometry_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, null=True),
        ),
    ]
