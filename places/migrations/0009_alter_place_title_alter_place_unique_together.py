# Generated by Django 4.2.6 on 2023-10-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_remove_place_description_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
        migrations.AlterUniqueTogether(
            name='place',
            unique_together={('longitude', 'latitude')},
        ),
    ]