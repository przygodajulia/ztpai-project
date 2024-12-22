from django.urls import path
from . import views

# TODO Why do we need a urls.py file also in app?
urlpatterns = [
    path("/name/<str:name>", views.home),
]