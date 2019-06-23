from django.forms import ModelForm, HiddenInput
from .models import Drink, DrinkReview

class DrinkForm(ModelForm):
    class Meta:
        model = Drink 
        fields = ['name','desc','img_url']

class DrinkReviewForm(ModelForm):
    class Meta:
        model = DrinkReview
        fields = ['drink', 'rating']
        widgets = {'drink': HiddenInput()}