from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from your first Django Backend 🚀")

def about(request):
    return HttpResponse("About this website")

def contact(request):
    return HttpResponse("Contact Page")

def say_hello(request, name):
    return HttpResponse(f"Hello, {name}, welcome to Django!")