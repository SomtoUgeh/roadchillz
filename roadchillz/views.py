from roadchillz.models import Restaurant
from django.shortcuts import redirect, render
from django.http import HttpResponse
from roadchillz.models import Restaurant, Category, Item
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def index(request):
    return render(request, 'roadchillz/index.html')

def categories(request):
    return render(request, 'roadchillz/categories.html')


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


def signup(request):
    return render(request, 'roadchillz/signup.html')
