from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponse, JsonResponse
from .models import Country, Project

def invest(request):
    return render(request, "initial_map.html")

def index(request):
    return render(request, "index.html")

def country(request, country):
    all_country_data = Country.objects.all()
    for country_data in all_country_data:
        if country_data.name == country:
            break
    
    all_project_data= Project.objects.all()
    project_data = []
    for y in all_project_data:
        if y.country == country_data:
            project_data.append(y)

    state = {
        "country": country_data.name,
        "description" : country_data.description,
        "emoji" : "🇦🇴",
        "data" : project_data
    }
    return render(request, "detail.html", state)
