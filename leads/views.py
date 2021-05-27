from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    # return HttpResponse("Hello hi glen")
    # return render(request, 'leads/home_page.html')
    context = {
        "name": "glen",
        "age": 23
    }
    return render(request, "second_page.html", context)
