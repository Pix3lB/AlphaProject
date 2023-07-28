
var DealerSum=0
var PlayerSum=0
var PlayerAce=0
var DealerAce=0
const PlayerHand=[]
const DealerHand=[]
deck = [];
window.onload = function() {
    buildDeck();
    shuffleDeck();
}
function StartGame(){
    DealCards()
    if (PlayerSum==21 || DealerSum==21){
        Stand();
    } 
    // console.log("The dealers hand is =",DealerHand);
    // console.log("The Players hand is =",PlayerHand);   
    // console.log("DealerSum",DealerSum);
    // console.log("PlayerSum",PlayerSum);
    document.getElementById("StartGame").disabled = true;
    document.getElementById("Hit").addEventListener("click", Hit,);
    document.getElementById("Stand").addEventListener("click", Stand,);
}
document.getElementById("StartGame").addEventListener ("click", StartGame, false);
function buildDeck() { 
    let values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];
    let types = ["♣", "♦", "♥", "♠"];
    deck = [];
    for (let i = 0; i < types.length; i++) {
        for (let j = 0; j < values.length; j++) {
            deck.push(values[j] + "-" + types[i]); 
        }
    }
}
function shuffleDeck() 
{ 
    //shuffles the deck
    for (let i = 0; i < deck.length; i++) {
        let j = Math.floor(Math.random() * deck.length); 
        let temp = deck[i];
        deck[i] = deck[j];
        deck[j] = temp;
    }
    // console.log(deck);
}
function DrawCard(n,hand,address){
    for (let i = 0; i < n; i++)
        {hand.push(deck.pop());
        if (address=="PlayerHand")
            {PlayerSum+= getValue(hand[hand.length-1]);
            PlayerAce += checkAce(hand[hand.length-1]);
            if (PlayerSum>21 && PlayerAce>0){
                PlayerSum-=10;
                PlayerAce-=1;
            }}
        else
            {DealerSum+=getValue(hand[hand.length-1]);
            DealerAce+= checkAce(hand[hand.length-1]);
            if (DealerSum>21 && DealerAce>0){
                DealerSum-=10;
                DealerAce-=1;
            }}
        rendercard(hand[hand.length-1],address);
        }
}
function DealCards(){
    DrawCard(2,DealerHand,"DealerHand");
    DrawCard(2,PlayerHand,"PlayerHand");
    const cardElement = document.getElementById('card1');
    cardElement.style.color = 'transparent';

}
function Hit(){
    DrawCard(1,PlayerHand,"PlayerHand",1)
}
function Stand(){
    const cardElement = document.getElementById('card1');
    cardElement.style.color = '';
    document.getElementById("Hit").disabled = true;
    document.getElementById("Stand").disabled = true;
    let message="";
    if (PlayerSum>21)   {message ="You Lose";}
    else if (PlayerSum==21)  { message ="BlackJack!! You win"}
    while (DealerSum<PlayerSum && DealerSum<=17){
        DrawCard(1,DealerHand,"DealerHand")}
    if(DealerSum>PlayerSum && DealerSum<=21){ message ="Dealer Won"}
    else if (DealerSum==PlayerSum){ message ="Push its a tie"}
    else { message ="You win Dealer Bust"}
   
    document.getElementById("Result").innerText = message;
    document.getElementById("reload").innerHTML = "Restart";
}
function getValue(card) {
    // console.log("getValue card",card);
    value=card.slice(0,-2);
    if (isNaN(value)) { //A J Q K
        if (value == "A") {
            return 11;

        }
        return 10;
    }
    return parseInt(value);
}
function checkAce(card) {
    if (card[0] == "A") {
        return 1;
    }
    return 0;
}

let cardCounter = 0; // Initialize the card counter variable

function createCardElement(card) {
    const rank = card.slice(0, -2);
    const suit = card.slice(-1);
    const color = (suit === '♦' || suit === '♥') ? 'red' : 'black';

    const cardElement = document.createElement('div');
    cardElement.className = 'card ' + color;
    
    cardCounter++; // Increment the card counter for each new card
    cardElement.id = 'card' + cardCounter; // Set a unique ID for the card
    
    cardElement.textContent = rank + '\n' + suit;

    return cardElement;
}

function rendercard(card,address) {
    const HandContainer = document.getElementById(address);
        const cardElement = createCardElement(card);
        HandContainer.appendChild(cardElement);
}
