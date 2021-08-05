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

    long = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    lat = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    location_name = forms.CharField(widget=forms.HiddenInput(), required=False)
    open_time = forms.DateField(
        label = 'Open Time',
        widget=forms.DateInput(attrs={'class':'form-control timepicker'}))
    close_time = forms.DateField(
        label = 'Close Time',
        widget=forms.DateInput(attrs={'class':'form-control timepicker'}))
    category = forms.CharField(
        label = 'Category',
        widget = forms.Select( attrs = {'class':'form-control'},
                choices= [
                    ('', 'Select')
                ]
            )
        )
    cuisines = forms.CharField(
        label = 'Cuisines',
        widget = forms.Select( attrs = {'class':'form-control'},
                choices= [
                    ('', 'Select')
                ]
            )
        )

    class Meta:
        model = Restaurant
        fields = ('name','open_time',)


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
