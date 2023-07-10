# Generated by Django 4.2.3 on 2023-07-10 12:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0003_alter_movie_genre_alter_movie_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('ACTION', 'ACTION'), ('DRAMA', 'DRAMA'), ('COMEDY', 'COMEDY'), ('ROMANCE', 'ROMANCE')], max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='Images/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('ENGLISH', 'ENGLISH'), ('HINDI', 'HINDI')], max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('RECENTLY ADDED', 'RECENTLY ADDED'), ('MOST WATCHED', 'MOST WATCHED'), ('TOP RATED', 'TOP RATED')], max_length=100),
        ),
    ]