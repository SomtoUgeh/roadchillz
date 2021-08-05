from django.urls import path
from roadchillz import views


app_name = "roadchillz"

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants', views.list_restaurants, name='restaurants'),
    path('categories/', views.categories, name='categories'),
    path('categories/restaurants/', views.category_restaurants, name='category_restaurants'),
    path('categories/restaurants/single_restaurant', views.single_restaurant, name='single_restaurant'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('add-restaurant', views.add_restaurant, name='add_restaurant')
]