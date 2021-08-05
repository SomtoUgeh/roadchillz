from django.test import TestCase
from roadchillz.models import Category, Restaurant
from django.urls import reverse


def add_restaurant(name, location, open_time, closing_time, long, lat, category, cuisine, item, likes=0):
    restaurant = Restaurant.objects.get_or_create(name=name)[0]

    restaurant.location_name = location
    restaurant.open_time = open_time
    restaurant.close_time = closing_time
    restaurant.long = long
    restaurant.lat = lat
    restaurant.likes = likes
    restaurant.category = category
    restaurant.cuisine = cuisine
    restaurant.item = item
    restaurant.image_url = 'http://www.unsplash.com'

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

    add_restaurant('Restaurant 1', 'Location 1', '12:00', '23:00', '-1.23', '1.23', 'take away', '["burger", "canadian"]', '{"name": "hash brown", "price": "1.29" }', 2)
    add_restaurant('Restaurant 2', 'Location 1', '12:00', '23:00', '-1.23', '1.23', 'take away', '["burger", "canadian"]', '{"name": "hash brown", "price": "1.29" }', 2)
    add_restaurant('Restaurant 3', 'Location 1', '12:00', '23:00', '-1.23', '1.23', 'take away', '["burger", "canadian"]', '{"name": "hash brown", "price": "1.29" }', 2)

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
    Example: "Random Restaurant String" should be "random-restaurant-string".
    """

    restaurant = add_restaurant('Very good food', 'Location 1', '12:00', '23:00', '-1.23', '1.23', 'take away', '["burger", "canadian"]', '{"name": "hash brown", "price": "1.29" }', 2)
    restaurant.save()

    self.assertEqual(restaurant.slug, 'very-good-food')

  def test_ensure_likes_are_positive(self):
    """
    Ensures the number of likes received for a Restaurant are positive or zero.
    """

    restaurant = add_restaurant('Very good food', 'Location 1', '12:00', '23:00', '-1.23', '1.23', 'take away', '["burger", "canadian"]', '{"name": "hash brown", "price": "1.29" }', 2)

    self.assertEqual((restaurant.likes >=0), True)


class CategoryMethodTests(TestCase):
  def test_slug_line_creation(self):
    """
    Checks to make sure that when a category is created, an appropriate slug is created.
    Example: "Random Category String" should be "random-category-string".
    """
    category = add_category('Random Category String')
    category.save()

    self.assertEqual(category.slug, 'random-category-string')
