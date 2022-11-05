from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponse, JsonResponse



def invest(request):
    return render(request, "initial_map.html")

def index(request):
    return render(request, "index.html")
