import random

class Card:
    """ represents a standared playing card
        clubs = 0 diamonds =1 hearts =2 spades =3
        jack queen and king are 11 12 13 ace =14 and then cards are 2-10
"""
    def __init__(self, suit=0,rank=2):
        self.suit =suit
        self.rank = rank
        
    suit_names=["Clubs","Diamonds","Hearts","Spades"]
    rank_names=[None,None,'2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])
      
    def is_better(self,other):
        if self.rank > other.rank:
            return True
        else:
            return False
        
    def is_same(self,other):
        if self.rank == other.rank:
            return True
        else:
            return False
        
        
class Deck:
    
    def __init__(self):
        self.cards =[]
        for suit in range(4):
            for rank in range(2,15):   #needed to change this 2thrugh14
                card = Card(suit,rank)
                self.cards.append(card)
                
    def __str__(self):
        res =[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def pick(self):
        return self.cards.pop()  ## pop(0) the card at index 0 but as in cards we should take the one on top wich is the bottom of  the list 
    
    def count(self):
        return len(self.cards)
    
    def add_card(self,card):
        return self.cards.insert(0,card)  ## could not use append cause we are picking from bottom with pop() we must add to the top
    
    def deal_war(self,hand1,hand2):
        for crd in range(26):  ## dealing 2 cards eachtime
          hand1.add_card(self.cards.pop())   ## did not use the venier pick just used the buit in method pop
          hand2.add_card(self.cards.pop())
          
            
    
class Hand(Deck):   ##inherits methods from deck so print
    def __init__(self,label=''):
        self.cards = []
        self.label = label
        
"""
>>> myhand = Hand('greg')
>>> card1 = deck2.pick()
>>> myhand.cards
[]
>>> myhand.add_card(card1)     from deck
>>> myhand.cards
[<__main__.Card object at 0x01EA6FD0>]
>>> print(myhand.cards)
[<__main__.Card object at 0x01EA6FD0>]
>>> myhand
<__main__.Hand object at 0x01EAD150>
>>> print(myhand)    from deck prints in the list
10 of Spades

>>> myhand = Hand('greg')
>>> yourhand = Hand('mj')
>>> wardeck = Deck()
>>> wardeck.shuffle()
>>> myhand.count()
0
>>> wardeck.count()
52
>>> wardeck.deal_war(myhand,yourhand)
>>> wardeck.count()
0
>>> myhand.count()
26

>>> yourhand.count()
26

>>> print(myhand[0])

Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'Hand' object does not support indexing   !!! you cannot get index of the object

>>> myhand.cards[0]
<__main__.Card object at 0x01EDE310>      !! but you can get the index of the values in the object which is a list

>>> print(myhand.cards[0])         !!! like this
10 of Clubs
>>> 


myhand = Hand('greg')
yourhand = Hand('mj')
wardeck = Deck()
wardeck.shuffle()
print('deck count',wardeck.count())
print('hand count',myhand.count())
wardeck.deal_war(myhand,yourhand)
print('dealing......')
print('deck count',wardeck.count())
print('hand count',myhand.count())

print(myhand)

"""

 
