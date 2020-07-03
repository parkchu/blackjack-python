class Player(object):
    def __init__(self,name, money, hand, bet):
        self.hand = hand
        self.name = name
        self.money = money
        self.bet = bet

    def betting(self):
        bet = int(input())
        if bet > self.money:
            error = int("error")

        elif bet <= self.money:
            self.bet = bet
            self.money -= bet

    def showHand(self):
        hand = ""
        for x in self.hand:
            hand += x.name
        return hand
    
    def whetherHit(self):
        whether = input()
        if whether == "hit":
            return True
        elif whether == "stay":
            return False
        
    def resetHand(self):
        self.hand = []

    def win(self):
        self.money += self.bet * 2

    def draw(self):
        self.money += self.bet
       
