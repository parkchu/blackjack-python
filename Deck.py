import random

class Deck(object):
    def __init__(self, cards):
        self.cards = cards
        self.use_cards = []
        
    def resetDeck(self):
        self.cards = self.cards + self.use_cards

    def shuffleDeck(self):
        random.shuffle(self.cards)

    def giveCard(self, someone):
        someone.hand.append(self.cards[0])
        self.use_cards.append(self.cards[0])
        del self.cards[0]
        
class Card(object):
    def __init__(self, name, num):
        self.name = name
        self.num = num
        
def makeDeck():
    cards = []
    shape = ['♠', '♣', '♥', '◈']
    for x in shape:
        for y in range(1, 14):
            if y == 1:
                cards.append(Card("{}A".format(x), y))

            elif y == 11:
                cards.append(Card("{}J".format(x), 10))
 
            elif y == 12:
                cards.append(Card("{}Q".format(x), 10))

            elif y == 13:
                cards.append(Card("{}K".format(x), 10))

            else:
                cards.append(Card("{}{}".format(x,y), y))
                
    return Deck(cards)
        
