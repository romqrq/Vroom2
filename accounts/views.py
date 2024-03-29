from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm


def login_view(request):
    """Return Login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Your have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None,
                                     "Username or password is incorrect.")

    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {'login_form': login_form})


@login_required
def logout_view(request):
    """Logs out the user"""

    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))


def register_view(request):
    """Loads registration page"""
    registration_form = UserRegistrationForm()
    return render(request, "register.html",
                  {'registration_form': registration_form})
