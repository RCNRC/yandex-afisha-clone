# Generated by Django 3.2.18 on 2023-05-01 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_place_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Place',
        ),
    ]
