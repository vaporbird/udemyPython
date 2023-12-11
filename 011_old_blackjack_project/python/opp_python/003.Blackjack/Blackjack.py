#vaporbird 30.10.2023
#this is a Blackjack game with jokers. Whoever draws a joker first wins on the spot. It adds some spice to the game :)
#Assuming the deck is infinite
#Dealer draws the first card

#Its pretty badly made :(
import collections
from random import choice

def checkJoker(hand):
    joker = deck.checkscore(hand)
    if (joker == -1):
        endFlag = 1
    return joker     

endFlag = 0
Card = collections.namedtuple ('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range (2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
        self.ranks += ["Black Joker", "Colored Joker"] 
        self.cards += [Card("Black Joker","unsuited"), Card("Colored Joker","unsuited")] 
 
    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, position):
        return self.cards[position]
    
    def printdeck(self):
        print(self.cards)

    def getcardpoints(self, card):
        if card.rank in list(['J','Q','K']):
            return 10
        if card.rank == 'A':
            return 11
        if card.rank in list(["Black Joker", "Colored Joker"]):
            return -1
        return int(card.rank)

        
    def checkscore (self, hand):
        score = 0
        acesCount = 0
        for card in hand:
            #print(card)
            currentCardPoints = self.getcardpoints(card)
            if (currentCardPoints == -1):
                return -1
            
            if(currentCardPoints == 11):
                acesCount += 1

            score += currentCardPoints
            
        while(score > 21 and acesCount > 0):
            acesCount -= 1
            score -= 10
        return score

                   
    def checkwin (self, dealerScore, playerScore):
        if (dealerScore == -1): 
            return 1 #dealer draws first. That is why this is on top
        
        if (playerScore == -1): 
            return -1
        
        if(dealerScore > 21 and playerScore > 21):
            if(playerScore > dealerScore): return 1
            if(dealerScore > playerScore): return -1
            return 0
        
        if((dealerScore > playerScore and dealerScore <= 21) or playerScore > 21): return 1
        if((playerScore > dealerScore and playerScore <= 21) or dealerScore > 21): return -1
        return 0 
    
    def printwin(self, winner):
        if(winner == 1):
            print("Dealer Wins")
        elif(winner == -1):
            print("Player Wins")
        else:
            print("Game is a Draw")
    
deck = FrenchDeck()
print("Deck Size", print(deck.__len__()))
deck.printdeck()

dealerHand = [choice(deck)]
playerHand = [choice(deck), choice(deck)]
print("GAME STARTS")
print(" Dealer: ", dealerHand,"\n Player: ", playerHand)

winner = deck.checkwin(checkJoker(dealerHand), checkJoker(playerHand))
if(endFlag == 1):
    deck.printwin(winner)

draw = input('Draw a card? - Y/n: ')

while(not endFlag):
    while (draw not in list(['Y', 'y', 'N', 'n'])):
        draw = input('Please enter valid input - Y/n: ')
    while (draw == 'Y' or draw == 'y'):
        playerHand += [choice(deck)]
        print(" Dealer: ", dealerHand,"\n Player: ", playerHand)

        if(checkJoker(playerHand) > 21):
            endFlag = 1
            break
        else:
            draw = input('Draw a card? - Y/n: ')
            while (draw not in list(['Y', 'y', 'N', 'n'])):
                draw = input('Please enter valid input - Y/n: ')

    if (not endFlag):
        while(checkJoker(dealerHand) < 17 and checkJoker(dealerHand) != -1):  
            dealerHand += [choice(deck)]
            print(" Dealer: ", dealerHand,"\n Player: ", playerHand)
        endFlag = 1

winner = deck.checkwin(checkJoker(dealerHand), checkJoker(playerHand))
if(endFlag == 1):
    deck.printwin(winner)


