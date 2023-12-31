# Generated by Django 4.2.6 on 2023-10-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_placeimage_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
