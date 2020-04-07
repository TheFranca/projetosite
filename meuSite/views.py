from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


# Create your views here.

def post(request):
    return render(request, 'visual/post.html')


def about(request):
    return render(request, 'visual/about.html')


def contact(request):
    return render(request, 'visual/contact.html')



