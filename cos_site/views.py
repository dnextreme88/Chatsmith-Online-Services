# Core
from django.shortcuts import render


def index(request):
    return render(request, 'cos_site/index.html', {})


def dashboard_profile(request):
    return render(request, 'cos_site/dashboard_profile.html', {})


def focal(request):
    return render(request, 'cos_site/focal.html', {})


def plateiq(request):
    return render(request, 'cos_site/plateiq.html', {})


def persistiq(request):
    return render(request, 'cos_site/persistiq.html', {})


def smart_alto(request):
    return render(request, 'cos_site/smart_alto.html', {})


def knowledge_base(request):
    return render(request, 'cos_site/knowledge_base.html', {})
