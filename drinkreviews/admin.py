from django.contrib import admin

# Register your models here.
from .models import Drink, DrinkReview

admin.site.register(Drink)
admin.site.register(DrinkReview)