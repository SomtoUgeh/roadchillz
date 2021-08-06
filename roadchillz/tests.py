from django.test import TestCase
from roadchillz.models import Category, Restaurant, Item
from django.urls import reverse


new_restaurant = {
  'open_time': '7:00',
  'close_time': '20:00',
  'lat': '55.85862919690698',
  'long': '-4.256994633787019',
  'location_name': 'argyle street',
  'image_url': '/static/images/tim-hortons.jpg',
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
}


def add_restaurant(name, likes=0):
  category = Category.objects.get_or_create(name=name)[0]
  category.image_url = 'http://unsplash.com'

  restaurant = Restaurant.objects.get_or_create(
    name=name,
    category=category,
    likes=likes,
    open_time=new_restaurant['open_time'],
    close_time=new_restaurant['close_time'],
    lat=new_restaurant['lat'],
    long=new_restaurant['long'],
    image_url=new_restaurant['image_url'],
    location_name=new_restaurant['location_name'],
  )[0]

  restaurant.save()
  return restaurant


def add_category(name):
  category = Category.objects.get_or_create(name=name)[0]
  category.image_url = 'http://unsplash.com'

  category.save()
  return category


class IndexViewTests(TestCase):
  def test_index_view_with_no_restaurants(self):
    """
    If no restaurants exist, the appropriate message should be displayed.
    """
    response = self.client.get(reverse('roadchillz:index'))

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'There are no restaurants present.')
    self.assertQuerysetEqual(response.context['restaurants'], [])


  def test_index_view_with_restaurants(self):
    """
    Checks whether restaurants are displayed correctly when present.
    """
    add_restaurant('Restaurant 1', 2)
    add_restaurant('Restaurant 2', 4)
    add_restaurant('Restaurant 3', 6)

    response = self.client.get(reverse('roadchillz:index'))

    self.assertEqual(response.status_code, 200)

    self.assertContains(response, 'Restaurant 1')
    self.assertContains(response, 'Restaurant 2')
    self.assertContains(response, 'Restaurant 3')

    num_restaurants = len(response.context['restaurants'])
    self.assertEquals(num_restaurants, 3)


  def test_slug_line_creation(self):
    """
    Checks to make sure that when a restaurant is created, an appropriate slug is created.
    """
    restaurant = add_restaurant('Very good food', 2)
    restaurant.save()

    self.assertEqual(restaurant.slug, 'very-good-food')


  def test_ensure_likes_are_positive(self):
    """
    Ensures the number of likes received for a restaurant are positive or zero.
    """
    restaurant = add_restaurant('Very good food', 2)
    restaurant.save()

    self.assertEqual((restaurant.likes >= 0), True)


class CategoryMethodTests(TestCase):
  def test_slug_line_creation(self):
    """
    Checks to make sure that when a category is created, an appropriate slug is created.
    Example: "Random Category String" should be "random-category-string".
    """
    category = add_category('Random Category String')
    category.save()

    self.assertEqual(category.slug, 'random-category-string')
