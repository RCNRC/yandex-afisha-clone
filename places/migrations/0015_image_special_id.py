# Generated by Django 3.2.18 on 2023-05-01 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_auto_20230501_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='special_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]