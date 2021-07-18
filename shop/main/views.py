from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def news(request):
    return render(request, 'main/news.html')


def signin(request):
    return render(request, 'main/signin.html')


def signup(request):
    return render(request, 'main/sighup.html')


def pc(request):
    return render(request, 'main/pc.html')


def phone(request):
    return render(request, 'main/phone.html')


def accessories(request):
    return render(request, 'main/accessories.html')

