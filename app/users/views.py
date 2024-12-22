from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.views import View
from .forms import LoginForm, RegisterForm

class LoginRegisterView(View):
    def get(self, request, *args, **kwargs):
        # Create the login and register forms for GET request
        login_form = LoginForm()
        register_form = RegisterForm()
        return render(request, 'login_register.html', {'login_form': login_form, 'register_form': register_form})

    # def post(self, request, *args, **kwargs):
    #     # Determine which form was submitted (login or register)
    #     if 'login_submit' in request.POST:
    #         login_form = LoginForm(request.POST)
    #         register_form = RegisterForm()  # Reset register form on login attempt
    #         if login_form.is_valid():
    #             # Process the login form
    #             email = login_form.cleaned_data['email']
    #             password = login_form.cleaned_data['password']

    #             # Authenticate the user
    #             user = authenticate(request, username=email, password=password)
    #             if user is not None:
    #                 # Login the user
    #                 login(request, user)
    #                 return redirect('races')  # Redirect to a different page after login, for example: 'races'
    #             else:
    #                 messages.error(request, 'Invalid email or password.')

    #     elif 'register_submit' in request.POST:
    #         login_form = LoginForm()  # Reset login form on registration attempt
    #         register_form = RegisterForm(request.POST)
    #         if register_form.is_valid():
    #             # Process the registration form
    #             full_name = register_form.cleaned_data['full_name']
    #             email = register_form.cleaned_data['email']
    #             password = register_form.cleaned_data['password']

    #             # Check if the user already exists
    #             if get_user_model().objects.filter(email=email).exists():
    #                 messages.error(request, 'A user with this email already exists.')
    #             else:
    #                 # Create and save the new user
    #                 user = get_user_model().objects.create_user(
    #                     username=email, email=email, password=password
    #                 )
    #                 user.first_name = full_name
    #                 user.save()

    #                 # After successful registration, log the user in
    #                 login(request, user)
    #                 return redirect('races')  # Redirect to a different page after successful registration, for example: 'races'
    #         else:
    #             messages.error(request, 'Please correct the errors below.')

        # If the form is invalid or user is not authenticated, render the login page with error messages
        return render(request, 'login_register.html', {'login_form': login_form, 'register_form': register_form})
