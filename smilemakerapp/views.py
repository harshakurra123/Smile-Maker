from django.shortcuts import render
from smilemakerapp.models import Joke
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.

    
    
class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = "__all__"


class JokeSerializer(serializers.Serializer):
    id = serializers.CharField()
    joke_title = serializers.CharField()
    joke_description = serializers.CharField()
    joke_user = UserSerializer()

    class Meta:
        model = Joke
        fields = ['id', 'joke_title', 'joke_description', 'joke_user', 'joke_image_base64']

def jokelist(request):
    joke_record = Joke.objects.all()
    context = JokeSerializer(joke_record, many=True).data
    final_result = {}
    final_result["data"] = context
    return render(request, 'jokelist.html', final_result)

def login(request):
    """login."""
    return render(request, 'login.html', context={})
    # username=request.data.get("username")
    # password=request.data.get("password")
    # user = authenticate(username=username, password=password)
    # if user is not None:
    #     return Response("user is authenticated")
    # else:
    #     return Response("login error")


def likepost(request):
    joke_id = request.data.get("joke_id")
    user_id = request.data.get("user_id")
    joke_record = Joke.objects.get(id=user_id)
    joke_record.joke_likes.add(user_id)
    joke_record.save()
    return HttpResponse('<h1>liked successfully</h1>')


def jokeRandom(request):
    """
    JokeRandom
    """
    joke_record = Joke.objects.order_by('?').first()
    context = JokeSerializer(joke_record).data
    print(context)
    return render(request, 'index.html', context)

def reverse(request):
    return redirect('')


def addjoke(request):
    """
    addjoke
    """
    return render(request, 'addjoke.html', context={})

def jokestatus(request):
    """jokestatus"""
    if request.method=="POST":
        print(request)
        title = request.POST.get("title")
        description = request.POST.get("description")
        joke_instance = Joke()
        joke_instance.joke_title = title
        joke_instance.joke_description = description
        joke_instance.joke_user_id = 1
        joke_instance.save()
        return redirect('/')

class JokeList(APIView):
    """
    Joke
    """
    def get(self, request):
        jokes_records = Joke.objects.all()
        jokes_serializer = JokeSerializer(jokes_records, many=True).data
        return Response(jokes_serializer, status=200)


class JokeCreate(APIView):
    """
    JokeCreate
    """
    def post(self, request):
        joke_instance = Joke()
        joke_instance.joke_title = request.data.get("joke_title")
        joke_instance.joke_description = request.data.get("joke_description")
        joke_instance.save()
        return Response({"status":"Joke created successfully"}, status=200)


        