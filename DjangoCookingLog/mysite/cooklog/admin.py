from django.contrib import admin

from .models import Chef, Dish_Photo, Dish, Ingredient, Recipe

class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 3

class ChefAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]

admin.site.register(Chef, ChefAdmin)

class DishInline(admin.TabularInline):
    model = Dish
    extra = 3

class RecipeAdmin(admin.ModelAdmin):
    inlines = [DishInline]

admin.site.register(Recipe, RecipeAdmin)

class DishIngredientInline(admin.TabularInline):
    model = Dish.ingredient_id.through

class DishAdmin(admin.ModelAdmin):
    inlines = [DishIngredientInline]
    search_fields = ['dish_name']
#    inlines = [Dish_Ingredients]

admin.site.register(Dish, DishAdmin)

class IngredientAdmin(admin.ModelAdmin):
    extra = 3 # doesn't seem used.

admin.site.register(Ingredient, IngredientAdmin)

#class DishesInline(admin.StackedInline):
#    model = Dishes

#class IngredientsInline(admin.StackedInline):
#    model = Ingredients

#class Dish_IngredientsAdmin(admin.ModelAdmin):
#    inlines = [
#        DishesInline,
#        IngredientsInline
#    ]

#admin.site.register(Dish_Ingredients, Dish_IngredientsAdmin)
