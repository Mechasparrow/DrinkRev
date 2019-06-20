from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'drinkreviews/index.html',{})

def view(request):
    return render(request, 'drinkreviews/view_drink.html', {})