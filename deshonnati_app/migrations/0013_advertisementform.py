# Generated by Django 2.2.3 on 2020-12-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deshonnati_app', '0012_bottomadds_topadds'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_address', models.CharField(max_length=200)),
                ('client_number', models.CharField(max_length=15)),
                ('client_agent_name', models.CharField(max_length=100)),
            ],
        ),
    ]
