# Generated by Django 3.2.18 on 2023-05-01 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=201),
        ),
    ]
