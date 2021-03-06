# Generated by Django 2.2.3 on 2022-06-19 06:24

import cloudinary.models
import deshonnati_app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deshonnati_app', '0015_auto_20220618_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyfeed',
            name='page10',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='page10'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyfeed',
            name='page11',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='page11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyfeed',
            name='page12',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='page12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyfeed',
            name='page2',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='page2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyfeed',
            name='page3',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='page3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyfeed',
            name='page4',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='page4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyfeed',
            name='page5',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='page5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyfeed',
            name='page6',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='page6'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyfeed',
            name='page7',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='page7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyfeed',
            name='page8',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='page8'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyfeed',
            name='page9',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='page9'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dailyfeed',
            name='page1',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='page1'),
        ),
        migrations.CreateModel(
            name='TestDailyFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('page1', models.FileField(upload_to=deshonnati_app.models.user_directory_path)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deshonnati_app.City')),
            ],
        ),
    ]
