from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Drink, DrinkReview

# Create your views here.
def index(request):
    drinks = Drink.objects.all()

    return render(request, 'drinkreviews/index.html',{'drinks': drinks})

def view(request, pk):
    drink_obj = Drink.objects.get(pk=pk)
    return render(request, 'drinkreviews/view-drink.html', {'drink': drink_obj})

def review(request):
    return render(request, 'drinkreviews/drink-review.html', {})

def create(request):
    return render(request, 'drinkreviews/create-drink.html', {})