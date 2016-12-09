from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the cooking log index.")

def chef_detail(request, chef_id):
    return HttpResponse("You're looking at chef with chef_id %s." % chef_id)

def recipe_detail(request, recipe_id):
    response = "You're looking at the recipe with recipe_id of %s."
    return HttpResponse(response % recipe_id)
