from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

CATEGORY_CHOICES = (
    ('ACTION','ACTION'),
    ('DRAMA','DRAMA'),
    ('COMEDY','COMEDY'),
    ('ROMANCE','ROMANCE'),
)


LANGUAGE_CHOICES = (
    ('ENGLISH','ENGLISH'),
    ('HINDI','HINDI'),
)


STATUS_CHOICES = (
    ('RECENTLY ADDED','RECENTLY ADDED'),
    ('MOST WATCHED','MOST WATCHED'),
    ('TOP RATED','TOP RATED'),
)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/')
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=100)
    status = models.CharField(choices=STATUS_CHOICES, max_length=100)
    views_count = models.IntegerField(default=0)
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)], default=0)
    description = models.TextField(default=None)

    def __str__(self):
        return self.title + " movie"
    


