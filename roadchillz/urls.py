from django.urls import path
from roadchillz import views


app_name = "roadchillz"

urlpatterns = [
    path('', views.index, name='index'),
]
