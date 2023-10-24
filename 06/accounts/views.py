from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('board:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_http_methods(['POST'])
def logout(request):
    # if not request.user.is_authenticated:
    #     return redirect('accounts:login')
    
    auth_logout(request)
    return redirect('boards:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['POST'])
def follow(request, user_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    me = request.user
    you = get_user_model().objects.get(pk=user_pk)

    if me != you:
        if me not in you.followers.all():
            you.followers.add(me)
        else:
            you.followers.remove(me)
    return redirect('accounts:profile', you.username)


@require_http_methods(['GET'])
def profile(request, username):
    person = get_user_model().objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)