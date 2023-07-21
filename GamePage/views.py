from django.shortcuts import render
from django.http import HttpResponse
import random
Deck=[]
def GamePage(request):
    DeckBuild(Deck)
    random.shuffle(Deck)
    StartGame()
    return render(request, 'GamePage.html')

def DeckBuild(deck):
    values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suit=["C", "D", "H", "S"]
    for i in suit:
        for j in values:
            deck.append(i+j)
def StartGame():
    Hidden=Deck.pop()
    DealerValue=+GetValue(Hidden)
    print("DealerValue\n",DealerValue)
    print("Hidden\n",Hidden)
def GetValue(card):
    if card[-1]=='A':
        return(11)
    elif card[-1]=='K' or card[-1]=='J' or card[-1]=='Q':
        return(10)
    else:
        return(int(card[-1]))