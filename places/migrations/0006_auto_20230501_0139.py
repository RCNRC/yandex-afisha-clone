# Generated by Django 3.2.18 on 2023-05-01 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='content',
            field=models.ImageField(max_length=210, upload_to=None),
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place'),
        ),
    ]