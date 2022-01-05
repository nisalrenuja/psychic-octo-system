from django.shortcuts import render
from django.http import HttpResponse, response


def index(request):
    return HttpResponse("hello my name is Nisal.")

def detail(request,question_id):
    return HttpResponse("You are looking at question %s."%question_id)

def results(request,question_id):
    response = "You're looking at results of the question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s." % question_id)