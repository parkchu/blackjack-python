class Dealer(object):
    def __init__(self, hand, deck):
        self.hand = hand
        self.deck = deck

    def gameStart(self, players):
        self.deck.resetDeck()
        self.deck.shuffleDeck()
        for x in range(2):
            for y in players:
                self.playerGetCard(y)
                if y == players[-1]:
                    self.getCard()
                    
    def playerGetCard(self, player):
        self.deck.giveCard(player)

    def getCard(self):
        self.deck.giveCard(self)

    def showHand(self):
        hand = ""
        for x in self.hand:
            hand = hand + x.name
        return hand
    
    def resetHand(self):
        self.hand = []
  
    def whetherGetCard(self, total_score):
        if total_score < 17:
            return True

        elif total_score >= 17:
            return False
