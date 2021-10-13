from django.urls import path
from . import views


urlpatterns = [
    path('', views.jokeRandom, name='index'),
    path('jokelist/', views.jokelist, name='jokelist'),
    path('reverse/', views.reverse, name='reverse'),
    path('joke/', views.JokeList.as_view()),

]