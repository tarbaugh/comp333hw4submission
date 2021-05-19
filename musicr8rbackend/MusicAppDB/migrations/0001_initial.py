# Generated by Django 3.1.7 on 2021-03-16 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistAttributes',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=255)),
                ('birth_location', models.CharField(max_length=255)),
                ('birth_year', models.IntegerField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('song', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='MusicAppDB.artistattributes')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='MusicAppDB.artists')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='MusicAppDB.users')),
            ],
        ),
    ]