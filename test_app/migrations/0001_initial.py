# Generated by Django 4.1.2 on 2022-10-10 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating_field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy', models.CharField(max_length=200)),
                ('checkIn', models.CharField(max_length=200)),
                ('cleanliness', models.CharField(max_length=200)),
                ('communication', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ScrapedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_id', models.CharField(max_length=200)),
                ('name_of_isting', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('bedrooms', models.CharField(max_length=200)),
                ('bathrooms', models.CharField(max_length=200)),
                ('beds', models.CharField(max_length=200)),
                ('accomodation_total', models.CharField(max_length=200)),
                ('listing_amenmodels', models.CharField(max_length=200)),
                ('host_name', models.CharField(max_length=200)),
                ('host_id', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('room_type', models.CharField(max_length=200)),
                ('picture_url', models.CharField(max_length=200)),
                ('ratings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.rating_field')),
            ],
        ),
    ]
