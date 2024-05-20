from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    founded_year = models.IntegerField()
    website = models.URLField()

    def __str__(self):
        return self.title

class Book (models.Model):

    CATEGORY_CHOICES = [
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
        ('biography', 'Biography'),
        ('classic', 'Classic'),
        ('drama', 'Drama'),
        ('history', 'History'),
    ]

    COVER_CHOICES = [
        ('soft', 'Softcover'),
        ('hard', 'Hardcover'),
    ]

    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    image = models.ImageField(upload_to='book_images/')
    publication_year = models.IntegerField()
    publisher = models.CharField(max_length=50)
    pages = models.IntegerField()
    dimensions = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    cover_type = models.CharField(max_length=4, choices = COVER_CHOICES)
    category = models.CharField(max_length=10, choices = CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title