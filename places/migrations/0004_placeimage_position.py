# Generated by Django 4.2.6 on 2023-10-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_placeimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeimage',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
