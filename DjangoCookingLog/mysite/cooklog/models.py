import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class Chef(models.Model):
    chef_id = models.AutoField(primary_key=True)
    email = models.CharField("Email address", max_length=50)
    first_name = models.CharField("First name", max_length=30)
    last_name = models.CharField("Last name", max_length=30)
    date_created = models.DateTimeField("Date created")
    def __str__(self):
        return self.first_name

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField("Recipe name", max_length=200)
    recipe_source = models.CharField("Recipe source", max_length=200)
    recipe_type = models.CharField(max_length=30)
    chef_id = models.ForeignKey(Chef, on_delete=models.CASCADE)
    date_created = models.DateTimeField("Date created")
    def __str__(self):
        return self.recipe_name

class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField("Ingredient name", max_length=30)
    ingredient_type = models.CharField("Ingredient type", max_length=30)
    date_created = models.DateTimeField("Date created")
    def __str__(self):
        return self.ingredient_name

class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    dish_name = models.CharField("Dish name", max_length=200)
    dish_details = models.CharField("Dish details", max_length=600)
    dish_rating = models.IntegerField(default=0)
    ingredient_id = models.ManyToManyField(Ingredient)
    date_created = models.DateTimeField("Date created")
    def __str__(self):
        return self.dish_name

#class Recipe_Ingredients(models.Model):
#    recipe_ingredients_id = models.AutoField(primary_key=True)
#    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)
#    ingredient_id = models.ForeignKey(Ingredients, on_delete=models.CASCADE) # no many:many b/c new table
#    quantity = models.CharField("Ingredient quantity", max_length=10)
#    date_created = models.DateTimeField("Date created")
# No __str__(self) .. should there be?

#class Recipe_Method(models.Model):
#    recipe_method_id = models.AutoField(primary_key=True)
#    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#    method_text = models.CharField("Recipe method", max_length=500)
#    date_created = models.DateTimeField("Date created")

#class Dish_Ingredients(models.Model):
#    dish_ingredient_id = models.AutoField(primary_key=True)
#    dish_id = models.ForeignKey(Dishes, on_delete=models.CASCADE)
#    ingredient_id = models.ForeignKey(Ingredients, on_delete=models.CASCADE) # no many:many here b/c new table
#    quantity = models.CharField("Ingredient quantity", max_length=10)
#    date_created = models.DateTimeField("Date created")

class Dish_Photo(models.Model):
    dish_photo_id = models.AutoField(primary_key=True)
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)
    photo_source = models.CharField("Photo url", max_length=200)
    date_created = models.DateTimeField("Date created")






#
#
#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#    def __str__(self):
#        return self.question_text
#    def was_published_recently(self):
#        now = timezone.now()
#        return now - datetime.timedelta(days=1) <= self.pub_date <= now
#    was_published_recently.admin_order_field = 'pub_date'
#    was_published_recently.boolean = True
#    was_published_recently.short_description = 'Published recently?'
#
#
#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
#    def __str__(self):
#        return self.choice_text
