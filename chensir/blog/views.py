from django.shortcuts import render

from blog.models import Article


# Create your views here.
def index(request):
    return render(request, 'index.html')


def python(request):
    python_title = Article.objects.filter(tag="python")
    return render(request, 'python.html', {"python_title": python_title})
    return render(request, 'python.html')


def django(request):
    django.title = Article.objects.filter(tag="django")
    return render(request, 'python.html', {"django_title": django.title})
    return render(request, 'django.html')


def scrapy(request):
    scrapy_title = Article.objects.filter(tag="scrapy")
    return render(request, 'python.html', {"scrapy_title": scrapy_title})
    return render(request, 'scrapy.html')


def all1(request):
    python_title = Article.objects.filter(tag="python")
    return render(request, 'python.html', {"python_title": python_title})


def er(request):
    return render(request, '1.html')
