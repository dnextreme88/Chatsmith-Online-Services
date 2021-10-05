# Core
from django.contrib import auth, messages
from django.shortcuts import redirect, render


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # If correct username and password, login the user
            auth.login(request, user)
            return redirect('dashboard_profile')
        else:
            # Neither username nor password is correct.
            messages.error(request, ' Unknown email address. Check again or try your username.')
            return redirect('login')

    return render(request, 'cos_site/index.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # If correct username and password, login the user
            auth.login(request, user)
            return redirect('dashboard_profile')
        else:
            # Neither username nor password is correct.
            messages.error(request, ' Unknown email address. Check again or try your username.')
            return redirect('login')

    return render(request, 'cos_site/login.html', {})


def logout(request):
    auth.logout(request)
    return render(request, 'cos_site/logout.html')


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
