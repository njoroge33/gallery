# Generated by Django 3.0 on 2019-12-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_description',
            field=models.CharField(max_length=250),
        ),
    ]
