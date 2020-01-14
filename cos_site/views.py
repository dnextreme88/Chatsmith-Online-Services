# Core
from django.shortcuts import render


def index(request):

    return render(request, 'cos_site/index.html', {})
