from roadchillz.models import Restaurant
from django.shortcuts import redirect, render
from django.http import HttpResponse
from roadchillz.models import Restaurant, Category, Item
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from roadchillz.forms import AddRestaurantForm

def index(request):
    return render(request, 'roadchillz/index.html')

def categories(request):
    context_dict = {}
    try:
        categories = Category.objects.all()
        context_dict['categories'] = categories
    except Restaurant.DoesNotExist:
        context_dict['categories'] = None
    return render(request, 'roadchillz/categories.html', context=context_dict)

def category_restaurants(request):
    return render(request, 'roadchillz/restaurants.html')

def single_restaurant(request):
    return render(request, 'roadchillz/single-restaurant.html')

def list_restaurants(request):
    context_dict = {}
    try:
        # checking related data
        # restaurants = Restaurant.objects.get(id=1)
        # print(restaurants.category)

        restaurants = Restaurant.objects.all()
        context_dict['restaurants'] = restaurants
    except Restaurant.DoesNotExist:
        context_dict['restaurants'] = None
    print(context_dict)
    return render(request, 'roadchillz/restaurants.html', context=context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('roadchillz:index'))
            else:
                return HttpResponse("Your Roadchillz account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'roadchillz/login.html')

def add_restaurant(request):

    form = AddRestaurantForm()

    if request.method == 'POST':
        form = AddRestaurantForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('roadchillz:index'))
        else:
            print(form.errors)
    return render(request, 'roadchillz/add-restaurant.html', {'form': form})


def signup(request):
    return render(request, 'roadchillz/signup.html')
