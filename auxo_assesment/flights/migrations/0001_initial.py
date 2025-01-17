# Generated by Django 3.2 on 2022-03-16 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('rating', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('airline_id', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('code', models.CharField(max_length=4, unique=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('itinerary_id', models.CharField(max_length=20, unique=True)),
                ('price', models.FloatField(default=0.0)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='agent', to='flights.agent')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Leg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('leg_id', models.CharField(max_length=20, unique=True)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('duration_mins', models.IntegerField()),
                ('stops', models.IntegerField(default=0)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='legs', to='flights.airline')),
                ('arrival_airport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='leg_arrival_airport', to='flights.airport')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='leg_departure_airport', to='flights.airport')),
                ('itineraries', models.ManyToManyField(related_name='legs', to='flights.Itinerary')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]
