from django import forms
from roadchillz.models import Restaurant, Category, Item, Cuisine
from django.contrib.auth.models import User
from roadchillz.models import UserProfile

class AddRestaurantForm(forms.ModelForm):
    name = forms.CharField(
        label = 'Name',
        max_length=Category.NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={'class':'form-control'}))

    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    likes = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    image_url = forms.CharField(
        widget=forms.HiddenInput(), 
        required=False,
        initial='/static/images/restaurant.jpg'
    )
    long = forms.CharField(
        widget=forms.HiddenInput(attrs={'id':'location-long'}), initial='100')
    lat = forms.CharField(
        widget=forms.HiddenInput(attrs={'id':'location-lat'}), initial='100')
    open_time = forms.CharField(
        label = 'Open Time',
        widget=forms.DateInput(attrs={'class':'form-control timepicker'}))
    close_time = forms.CharField(
        label = 'Close Time',
        widget=forms.DateInput(attrs={'class':'form-control timepicker'}))

    category = forms.ModelChoiceField(
        empty_label='Select',
        queryset=Category.objects.all().order_by('name'),
        widget = forms.Select( attrs = {'class':'form-control'}),
    )

    cuisine = forms.ModelChoiceField(
        queryset=Cuisine.objects.all().order_by('name'),
        widget = forms.Select( attrs = {'class':'form-control'}),
    )

    location_name = forms.CharField(
            label = 'Street/Area Name',
            max_length=Restaurant.NAME_MAX_LENGTH,
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
    
    class Meta:
        model = Restaurant
        fields = ('name','open_time', 'close_time', 'long', 'lat', 'category', 'location_name', 'image_url')


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
