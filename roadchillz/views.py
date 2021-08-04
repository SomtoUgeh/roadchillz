from roadchillz.models import Restaurant
from django.shortcuts import render
from django.http import HttpResponse
from roadchillz.models import Restaurant, Category, Item

def index(request):
    return HttpResponse("Hello world")


# Create your views here.

def list_restaurants(request):
    context_dict = {}
    try:
        # checking related data
        # restaurants = Restaurant.objects.get(id=1)
        # print(restaurants.category)

        restaurants = Restaurant.objects.all()
        context_dict['restaurants'] = restaurants
    except Category.DoesNotExist:
        context_dict['restaurants'] = None
    print(context_dict)
    return render(request, 'restaurants.html', context=context_dict)