from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello my name is Nisal. this is my second django practice project. And I am going to create poll application")