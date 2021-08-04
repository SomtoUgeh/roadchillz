from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    NAME_MAX_LENGTH = 64
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)

    def save (self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    NAME_MAX_LENGTH = 64
    IMAGE_URL_MAX_LENGTH = 128
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    long = models.FloatField()
    lat = models.FloatField()
    location_name = models.CharField(max_length=NAME_MAX_LENGTH)
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()
    image_url = models.CharField(max_length=IMAGE_URL_MAX_LENGTH)

    def __str__(self):
        return self.name

class Item(models.Model):
    NAME_MAX_LENGTH = 64
    IMAGE_URL_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    image_url = models.CharField(max_length=IMAGE_URL_MAX_LENGTH)
    price = models.BigIntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    NAME_MAX_LENGTH = 64
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    item = models.ManyToManyField(Restaurant)
    
    def __str__(self):
        return self.name