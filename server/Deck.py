from Card import Card
from random import randint

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        disp = {1: "Ace", 11: "Jack", 12: "Queen",13: "King"}

        for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for v in range(1,14):
                try:
                    self.cards.append(Card(s,disp[v]))
                except:
                    self.cards.append(Card(s,v))
    
    def shuffle(self, times=1):
        for t in range(0,times):
            for i in range(len(self.cards) - 1, 0, -1):
                r = randint(0,i)
                self.cards[i],self.cards[r] = self.cards[r],self.cards[i]
    
    def show(self):
        for c in self.cards:
            c.show()


