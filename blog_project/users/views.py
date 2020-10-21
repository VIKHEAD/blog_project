from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('HELLO')

def name(request, first_name):
    return HttpResponse(f"My first name is: {first_name}")

def surname(request, last_name):
    return HttpResponse(f'My last name is : {last_name}')

def age(request, user_age):
    return HttpResponse(f'Age : {user_age}')