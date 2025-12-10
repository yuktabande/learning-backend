from django.shortcuts import render
from datetime import datetime

def home(request):
    context = {
        "name": "Yukta",
        "date": datetime.now().date()
    }
    return render(request, "blog/home.html", context)

def about(request):
    context = {
        "items": ["AI", "Backend", "Cloud", "Django", "Systems"]
    }
    return render(request, "blog/about.html", context)

def say_hello(request, name):
    return render(request, "blog/hello.html", {"name": name})