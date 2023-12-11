#vaporbird 29.10.2023
#this code is far from optimal. Im just exploring and having fun :)
import collections
from random import choice

Card = collections.namedtuple ('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range (2,11)] +  list('JQKA') + ["test"]
    ranks.append('Instruction manual')
    suits= 'spades diamonds clubs hearts'.split()

    def __init__(self):
        #sone spamcode for testing
        correctCardranks = [rank for rank in self.ranks if rank != "test"] 
        self._cards = [Card(rank, suit) for suit in self.suits for rank in correctCardranks if rank != "Instruction manual"]
        self._cards += [Card("Black Joker", ""), Card("Colored Joker","")]
        self._cards.pop()
        self._cards += [Card("Colored Joker","")]

        #self._cards = [tuple(ele for ele in tester if ele != "") for tester in self._cards] #removes the empty string of the jokers
 
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def printcards(self):
        for card in self._cards:
            print(card)

    def spades_high(card):
        if (card.rank not in FrenchDeck.ranks):
            return -1 

        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]
      
deck = FrenchDeck()
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

print("*************")
for card in sorted(deck, key = FrenchDeck.spades_high, reverse=True):
    print(card)

print("*************")
print(card)
print(len(deck))
print(deck.__len__())
print(deck[15])
print(deck.__getitem__(15))

print(choice(deck))
print(choice(deck))
print(choice(deck))

