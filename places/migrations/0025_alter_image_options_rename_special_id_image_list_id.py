# Generated by Django 4.2 on 2023-05-07 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0024_alter_place_description_long_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['list_id']},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='special_id',
            new_name='list_id',
        ),
    ]
