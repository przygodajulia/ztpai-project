from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request, name):
    # Context data for login and register messages
    # loginMessages = []  # Get these from session or your logic
    # registerMessages = []  # Get these from session or your logic
    #
    # return render(request, '/templates/login_register.html', {
    #     'loginMessages': loginMessages,
    #     'registerMessages': registerMessages
    # })
    query = name
    return HttpResponse(f"<h1> {query} </h1>")