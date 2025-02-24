from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # http response
    return render(request, 'recipes\pages\home.html', context={'name': 'Jedson'})

