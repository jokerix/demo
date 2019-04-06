from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html')


def python(request):
    return render(request, 'python.html')


def django(request):
    return render(request, 'django.html')


def scrapy(request):
    return render(request, 'scrapy.html')
