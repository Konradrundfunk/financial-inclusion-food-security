from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponse, JsonResponse



def getting_score(request):

    if request.method is "POST":
        response = {
            "data": "Test Data",
            "farm": "example farm",
            "score": 123,
        }
        return JsonResponse(response)

    else:
        return HttpResponseNotAllowed("Not allowed")