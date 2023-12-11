#vaporbird 30.10.2023
#this is a Blackjack game with jokers. Whoever draws a joker first wins on the spot. It adds some spice to the game :)
#Assuming the deck is infinite
#Dealer draws the first card
#Dealer's hidden card is drawn after the player has finished drawing his hand.

import collections
from random import choice

class FrenchDeck:
    endFlag = 0
    Card = collections.namedtuple ('Card',['rank','suit'])
    ranks = [str(n) for n in range (2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [self.Card(rank, suit) for rank in self.ranks for suit in self.suits]
        self.ranks += ["Black Joker", "Colored Joker"] 
        self.cards += [self.Card("Black Joker","unsuited"), self.Card("Colored Joker","unsuited")] 
 
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

    def blackjack(self):
        print("Deck Size", print(self.__len__()))
        self.printdeck()
        dealerHand = [choice(self)]
        playerHand = [choice(self), choice(self)]
        print("GAME STARTS")
        print(" Dealer: ", dealerHand,"\n Player: ", playerHand)

        winner = self.checkwin(self.checkJoker(dealerHand), self.checkJoker(playerHand))
        if(self.endFlag == 1):
            self.printwin(winner)
        draw = input('Draw a card? - Y/n: ')
        while(not self.endFlag):
            while (draw not in list(['Y', 'y', 'N', 'n'])):
                draw = input('Please enter valid input - Y/n: ')
            while (draw == 'Y' or draw == 'y'):
                playerHand += [choice(self)]
                print(" Dealer: ", dealerHand,"\n Player: ", playerHand)

                if(self.checkJoker(playerHand) > 21):
                    self.endFlag = 1
                    break
                else:
                    draw = input('Draw a card? - Y/n: ')
                    while (draw not in list(['Y', 'y', 'N', 'n'])):
                        draw = input('Please enter valid input - Y/n: ')

            if (not self.endFlag ):
                while(self.checkJoker(dealerHand) < 17 and self.checkJoker(dealerHand) != -1):  
                    dealerHand += [choice(self)]
                    print(" Dealer: ", dealerHand,"\n Player: ", playerHand)
                self.endFlag = 1
        winner = self.checkwin(self.checkJoker(dealerHand), self.checkJoker(playerHand))
        if(self.endFlag == 1):
            self.printwin(winner)

    def checkJoker(self,hand):
        joker = self.checkscore(hand)
        if (joker == -1):
            self.endFlag = 1
        return joker 
    

deck = FrenchDeck()
deck.blackjack()






