# Generated by Django 3.2.18 on 2023-05-01 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_image_special_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='special_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
