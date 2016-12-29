from django.http import HttpResponse
#from django.http import Http404
#from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Dish

def index(request):
    return HttpResponse("Hello, world. You're at the cooking log index.")

def chef_detail(request, chef_id):
    return HttpResponse("You're looking at chef with chef_id %s." % chef_id)

def chef_entry(request):
    return HttpResponse("Here we could enter a new chef user.")

def recipe_detail(request, recipe_id):
    response = "You're looking at the recipe with recipe_id of %s."
    return HttpResponse(response % recipe_id)

def recipe_entry(request):
    return HttpResponse("Here we could enter new recipes.")

def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    return render(request, 'cooklog/dish_detail.html', {'dish': dish})

def dish_entry(request, recipe_id):
    response = "Here we could enter a new dish for recipe_id of %s."
    return HttpResponse(response % recipe_id)

def feed(request):
    latest_dish_list = Dish.objects.order_by('-date_created')[:5]
    #template = loader.get_template('cooklog/feed.html')
    context = {'latest_dish_list': latest_dish_list}
    return render(request, 'cooklog/feed.html', context)


