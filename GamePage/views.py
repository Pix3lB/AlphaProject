from django.shortcuts import render
from django.http import HttpResponse
import random
def GamePage(request):
    deck=[]
    DeckBuild(deck)
    print(deck)
    random.shuffle(deck)
    print(deck)
    return render(request, 'GamePage.html')

def DeckBuild(a):
    values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suit=["C", "D", "H", "S"]
    for i in suit:
        for j in values:
            a.append(i+j)

