from django.contrib import admin
from roadchillz.models import UserProfile, Restaurant, Category


class RestaurantAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}


admin.site.register(UserProfile)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Category, RestaurantAdmin)
