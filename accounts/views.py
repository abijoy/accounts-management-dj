from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .forms import CustomUserCreationForm, LoginForm

# Create your views here.
def index(request):
    if request.user.is_superuser:
        return HttpResponse(f'<h1> This is admin [{request.user.email}] dashboard </h1>')
    elif request.user.is_staff:
        return HttpResponse(f'<h1> This is staff [{request.user.email}] dashboard </h1>')
    else:
        return HttpResponse(f'<h1> This is user [{request.user.email}] dashboard </h1>')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request,
                                email=form.cleaned_data['email'],
                                password=form.cleaned_data['password1'])
            if user:
                login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print('############here ############')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email, password)
            print('------user----: ', user)
            if user is not None:
                login(request, user)
                return redirect('index')
    else: 
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})