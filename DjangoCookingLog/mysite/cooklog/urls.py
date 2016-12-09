from django.conf.urls import url

from . import views

urlpatterns = [
               # ex: /cooklog/
               url(r'^$', views.index, name='index'),
               # ex: /cooklog/5/chef/
               url(r'^(?P<chef_id>[0-9]+)/chef/$', views.chef_detail, name='chef'),
               # ex: /cooklog/5/recipes/
               url(r'^(?P<recipe_id>[0-9]+)/recipe/$', views.recipe_detail, name='recipe'),
               ]
