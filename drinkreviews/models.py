'''
EX:

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''
from django.db import models
from django.db.models import Avg

# Create your models here.

# Drink Model
class Drink(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    img_url = models.URLField()

    def __str__(self):
        return self.name

    @property
    def rating(self):
        reviews_rating = DrinkReview.objects.filter(drink=self).aggregate(Avg('rating'))['rating__avg']

        if (reviews_rating == None):
            reviews_rating = 0.0

        return reviews_rating


# DrinkReview model
class DrinkReview(models.Model):
    drink = models.ForeignKey(Drink, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)

    def __str__(self):
        return "Review for " + self.drink.name


