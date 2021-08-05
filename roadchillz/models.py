from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    NAME_MAX_LENGTH = 64
    IMAGE_URL_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    image_url = models.CharField(max_length=IMAGE_URL_MAX_LENGTH)
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
    open_time = models.TimeField()
    close_time = models.TimeField()
    image_url = models.CharField(max_length=IMAGE_URL_MAX_LENGTH)

    slug = models.SlugField(unique=True)
    likes = models.IntegerField(default=0)

    def save (self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

class Item(models.Model):
    NAME_MAX_LENGTH = 64
    IMAGE_URL_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    image_url = models.CharField(max_length=IMAGE_URL_MAX_LENGTH)
    price = models.FloatField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    NAME_MAX_LENGTH = 64

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    item = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
