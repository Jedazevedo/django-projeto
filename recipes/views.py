from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_view(request):
    # http response
    return HttpResponse("<h1>PAGINA INICIAL!</h1>")

def home_view(request):
    return HttpResponse("<h1>HOME!</h1>")

def sobre_view(request):
    return HttpResponse("<h1>SOBRE!</h1>")