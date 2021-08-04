from django.urls import path
from roadchillz import views


app_name = "roadchillz"

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants', views.list_restaurants, name='restaurants'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
]
