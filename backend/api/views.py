from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponse, JsonResponse



def invest(request):
    return render(request, "initial_map.html")

def index(request):
    return render(request, "index.html")

def country(request, country):
    state = {
        "country": country,
        "detail" : "Angola, is a country located on the west coast of Southern Africa. It is the second-largest Portuguese-speaking country in both total area and population, and is the seventh-largest country in Africa. It is bordered by Namibia to the south, the Democratic Republic of the Congo to the north, Zambia to the east, and the Atlantic Ocean to the west.",
        "emoji" : "🇦🇴",
        "data" : [
            {
                "headline" : "Projekt 1",
                "text": "123123123"
            }
        ]
    }
    return render(request, "detail.html", state)
