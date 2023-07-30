# Generated by Django 4.2 on 2023-05-02 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0019_alter_place_description_long"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="content",
            field=models.ImageField(max_length=210, upload_to="./images"),
        ),
        migrations.AlterField(
            model_name="place",
            name="title",
            field=models.CharField(max_length=201, unique=True),
        ),
    ]
