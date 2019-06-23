from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from django.template import loader

from .models import Drink, DrinkReview
from .forms import DrinkForm, DrinkReviewForm

# Create your views here.
def index(request):
    drinks = Drink.objects.all()

    return render(request, 'drinkreviews/index.html',{'drinks': drinks})

def view(request, pk):
    drink_obj = Drink.objects.get(pk=pk)
    return render(request, 'drinkreviews/view-drink.html', {'drink': drink_obj})

def review(request, pk):
    drink_to_review = Drink.objects.get(pk=pk)

    if request.method == 'POST':
        form = DrinkReviewForm(request.POST)
        print (form.is_valid())
        if form.is_valid():
            new_drink_review = form.save()
            return redirect('index')
    else:
        form = DrinkReviewForm({'drink': drink_to_review.id})

    return render(request, 'drinkreviews/drink-review.html', {'form': form,  'drink': drink_to_review})

def create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DrinkForm(request.POST)
        
        # check whether it's valid:
        print (form.is_valid())
        if form.is_valid():
            new_drink = form.save()
            return redirect('view', pk = new_drink.id)
    else:
        # Create an empty drink form
        form = DrinkForm()

    return render(request, 'drinkreviews/create-drink.html', {'form': form})