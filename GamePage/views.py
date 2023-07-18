from django.shortcuts import render
from django.http import HttpResponse

def GamePage(request):
    return render(request, 'GamePage.html')
