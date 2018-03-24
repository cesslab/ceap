from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm


def login_page(request):
    form = LoginForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/login')
        else:
            print("Error")

    return render(request, "accounts/login.html", context)
