from django.urls import path
from . import views


urlpatterns = [
    path('', views.jokeRandom, name='index'),
    path('jokelist/', views.jokelist, name='jokelist'),
    path('reverse/', views.reverse, name='reverse'),
    path('joke/', views.JokeList.as_view()),
    path('login/', views.login, name='login'),
    path('addjoke/', views.addjoke, name='addjoke'),
    path('jokestatus/', views.jokestatus, name='jokestatus'),

]