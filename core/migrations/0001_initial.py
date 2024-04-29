# Generated by Django 5.0.4 on 2024-04-09 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('license_number', models.CharField(max_length=20)),
                ('car_registration', models.CharField(max_length=20)),
                ('car_make', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='driver_images')),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('zipcode', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('adress', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('lat', models.CharField(blank=True, max_length=200, null=True)),
                ('lng', models.CharField(blank=True, max_length=200, null=True)),
                ('place_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]