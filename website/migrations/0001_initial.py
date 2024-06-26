# Generated by Django 5.0.4 on 2024-04-27 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('origin_city', models.CharField(max_length=100)),
                ('destination_city', models.CharField(max_length=100)),
                ('departure_date', models.DateField(max_length=50)),
                ('available_seats', models.CharField(max_length=50)),
                ('price', models.PositiveSmallIntegerField()),
                ('phone_number', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
            ],
        ),
    ]
