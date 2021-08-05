from roadchillz.models import Restaurant
from django.shortcuts import redirect, render
from django.http import HttpResponse
from roadchillz.models import Restaurant, Category, Item
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from roadchillz.forms import AddRestaurantForm
from roadchillz.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required

def index(request):
    context_dict = {}

    try:
        restaurants = Restaurant.objects.all()
        context_dict['restaurants'] = restaurants
    except Restaurant.DoesNotExist:
        context_dict['restaurants'] = None

    return render(request, 'roadchillz/index.html', context=context_dict)


def categories(request):
    context_dict = {}
    try:
        categories = Category.objects.all()
        context_dict['categories'] = categories
    except Category.DoesNotExist:
        context_dict['categories'] = None
    return render(request, 'roadchillz/categories.html', context=context_dict)


def category_restaurants(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        restaurants = Restaurant.objects.filter(category=category)

        context_dict['category'] = category
        context_dict['restaurants'] = restaurants
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['restaurants'] = None

    # Go render the response and return it to the client.
    return render(request, 'roadchillz/restaurants.html')


def single_restaurant(request, restaurant_name_slug):
    context_dict = {}

    try:
        restaurant = Restaurant.objects.get(slug=restaurant_name_slug)
        context_dict['restaurant'] = restaurant
    except Restaurant.DoesNotExist:
        context_dict['restaurant'] = None

    # Go render the response and return it to the client.
    return render(request, 'roadchillz/single-restaurant.html')


@login_required
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
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'roadchillz/signup.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


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


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('roadchillz:index'))
