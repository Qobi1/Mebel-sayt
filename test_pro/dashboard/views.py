from django.shortcuts import render

# Create your views here.


def home(requests):
    ctx = {}
    return render(requests, 'dashboard/index.html', ctx)
