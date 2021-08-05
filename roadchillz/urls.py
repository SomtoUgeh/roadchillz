from django.urls import path
from roadchillz import views


app_name = "roadchillz"

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/<slug:category_name_slug>', views.category_restaurants, name='category_restaurants'),
    path('restaurants/', views.index, name='restaurants'),
    path('restaurants/<slug:restaurant_name_slug>', views.single_restaurant, name='single_restaurant'),
    path('restaurants/add-restaurant', views.add_restaurant, name='add_restaurant'),
    path('categories/', views.categories, name='categories'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]
