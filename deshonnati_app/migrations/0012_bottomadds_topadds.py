# Generated by Django 2.2.3 on 2020-11-04 11:08

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deshonnati_app', '0011_pagetwoclip_two_clip_seven'),
    ]

    operations = [
        migrations.CreateModel(
            name='BottomAdds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottom_add_date', models.DateField()),
                ('bottom_add_one', cloudinary.models.CloudinaryField(max_length=255, verbose_name='two_clip_one')),
                ('bottom_add_two', cloudinary.models.CloudinaryField(max_length=255, verbose_name='two_clip_one')),
            ],
        ),
        migrations.CreateModel(
            name='TopAdds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField()),
                ('add_one', cloudinary.models.CloudinaryField(max_length=255, verbose_name='two_clip_one')),
                ('add_two', cloudinary.models.CloudinaryField(max_length=255, verbose_name='two_clip_one')),
            ],
        ),
    ]
