
from django.urls import path
from recipes.views import my_view, home_view, sobre_view

urlpatterns = [
    path('', my_view),
    path('home/', home_view),
    path('sobre/', sobre_view),
]