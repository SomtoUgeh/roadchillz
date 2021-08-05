from django import forms
from roadchillz.models import Restaurant, Category, Item, Cuisine

class AddRestaurantForm(forms.ModelForm):
    name = forms.CharField(
        label = 'Name',
        max_length=Category.NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={'class':'form-control'}))
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