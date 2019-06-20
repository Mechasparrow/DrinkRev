from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Drink, DrinkReview

# Create your views here.
def index(request):
    drinks = Drink.objects.all()

    return render(request, 'drinkreviews/index.html',{'drinks': drinks})

def view(request):
    return render(request, 'drinkreviews/view_drink.html', {})