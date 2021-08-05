import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'app.settings')

import django
django.setup()
from roadchillz.models import Category, Restaurant, Cuisine, Item
from datetime import datetime

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    cuisines = ['mexican', 'italian', 'canadian', 'chinese', 'american', 'indian', 'thai', 'nigerian', 'pizza', 'burger' ]
    categories = [
        {'name':'dine out', 'image_url': '/static/images/dine-out.jpg'}, 
        {'name': 'cafe', 'image_url': '/static/images/cafe.jpg'}, 
        {'name': 'pub', 'image_url': '/static/images/pub.jpg'}, 
        {'name':'night life', 'image_url': '/static/images/nightlife.jpg'}, 
        {'name': 'drinks', 'image_url': '/static/images/drinks.jpg'}, 
        {'name': 'take away', 'image_url': '/static/images/takeaway.jpg'}
    ]

    restaurants = [
        {
            'name': 'Tim Hortons - Argyle street',
            'open_time': '7:00',
            'close_time': '20:00',
            'lat': '55.85862919690698',
            'long': '-4.256994633787019',
            'location_name': 'argyle street',
            'category': 'take away',
            'cuisine': ['burger', 'canadian'],
            'items': [
                {
                    'name': 'hash brown',
                    'price': 1.29
                },
                {
                    'name': 'wrap meal',
                    'price': 7.5
                },
                {
                    'name': 'donuts',
                    'price': 12.5
                }
            ]
        },
        {
            'name': 'McDonalds - Tron gate',
            'open_time': '9:00',
            'close_time': '23:59',
            'lat': '55.85728851068552',
            'long': '-4.2462774609719265',
            'location_name': 'tron gate',
            'category': 'dine out',
            'cuisine': ['burger', 'american'],
            'items': [
                {
                    'name': 'egg mcmuffin',
                    'price': 2.99
                },
                {
                    'name': 'cheesy bacon flatbread',
                    'price': 3.09
                },
                {
                    'name': 'breakfast roll',
                    'price': 4.5
                }
            ]
        },
        {
            'name': 'Starbucks - Sauichiehall',
            'open_time': '11:00',
            'close_time': '18:00',
            'lat': '55.86439941126669',
            'long': '-4.254263703646989',
            'location_name': 'sauichiehall street',
            'category' : 'cafe',
            'cuisine': ['american'],
            'items': [
                {
                    'name': 'caffe latte',
                    'price': 3.85
                },
                {
                    'name': 'strawberry cream cake',
                    'price': 2.25
                },
                {
                    'name': 'butter croissant',
                    'price': 2.20
                }
            ]
        },
        {
            'name': 'Henleys Byre',
            'open_time': '10:00',
            'close_time': '19:00',
            'lat': '55.87133375020882',
            'long': '-4.298679735504694',
            'category' : 'dine out',
            'cuisine': ['italian', 'mexican'],
            'location_name': 'byres road',
            'items': [
                {
                    'name': 'hot filled roll',
                    'price': 3.00
                },
                {
                    'name': 'all day breakfast',
                    'price': 6.5
                },
                {
                    'name': 'meal deal',
                    'price': 9.0
                }
            ]
        }
    ]

    print('Starting db operations');

    for cat in categories:
        c = add_cat(cat)
    
    for cuisine in cuisines:
        cui = add_cuisine(cuisine)

    for restaurant in restaurants:
        # Handle via transactions
        # Create items
        r = Restaurant.objects.get_or_create(
            name=restaurant['name'], 
            category=Category.objects.get(name=restaurant['category']), 
            open_time=restaurant['open_time'],
            close_time=restaurant['close_time'],
            lat=restaurant['lat'],
            long=restaurant['long'],
            location_name=restaurant['location_name']
        )[0]
        for item in restaurant['items']:
            i = Item.objects.get_or_create(name=item['name'], price=item['price'], restaurant=r)[0]
    
    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Restaurant.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_cat(category_data):
    c = Category.objects.get_or_create(name=category_data['name'], image_url=category_data['image_url'])[0]
    c.save()
    return c

def add_cuisine(name):
    c = Cuisine.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Roadchillz population script...')
    populate()