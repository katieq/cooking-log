from django.conf.urls import url

from . import views

app_name = 'cooklog'
urlpatterns = [
               # ex: /cooklog/
               url(r'^$', views.index, name='index'),
               # ex: /cooklog/chef/4/
               url(r'^chef/(?P<chef_id>[0-9]+)/$', views.chef_detail, name='chef'),
               url(r'^new_chef/$', views.chef_entry, name='new_chef'),
               # ex: /cooklog/recipe/5/
               url(r'^recipe/(?P<recipe_id>[0-9]+)/$', views.recipe_detail, name='recipe'),
               url(r'^new_recipe/$', views.recipe_entry, name='new_recipe'),
               url(r'^dish/(?P<dish_id>[0-9]+)/$', views.dish_detail, name='dish_detail'),
               url(r'^new_dish/(?P<dish_id>[0-9]+)/$', views.dish_entry, name='new_dish'),
               url(r'^feed/$', views.feed, name='feed'),
               ]
