import random

class BlackJack(object):

    def __init__(self, cards, player, dealer):
        self.cards = cards
        self.player = player
        self.dealer = dealer

    def gameStart(self):
        for x in self.player:
            x.betting()
            x.cards = []
            self.dealer.cards = []
        self.dealer.giveCard(self.player, self.cards)
        for x in self.player:
            print("{}님은 {} 입니다. 카드를 더 받으시겠습니까? ('hit' or 'stay')".format(x.name, x.showHand()))
            while True:
                do = input()
                if do == "hit":
                    self.dealer.hit(x, self.cards)
                    if x.totalScore() > 21:
                        print("{}카드를 받으셔서 {}입니다. 21을 넘기셨습니다. 버스트입니다".format(x.cards[-1].name, x.showHand()))
                        x.bust = True
                        break
                    elif x.totalScore() <= 21:
                        print("{}카드를 받으셔서 {}입니다. 카드를 받으시겠습니까? ('hit' or 'stay')".format(x.cards[-1].name, x.showHand()))
                elif do == "stay":
                    break
        self.result()
        
    def result(self):
        dealerScore = self.dealer.totalScore()
        print("딜러의 카드는 {}입니다.".format(self.dealer.showHand()))
        self.dealer.openCard(self.cards)
        for x in self.player:
            playerScore = x.totalScore()
            print("{}님은".format(x.name))
            if x.bust:
                print("버스트입니다")
                print("소지한 금액이 {}으로 되었습니다".format(x.money))

            else:
                if self.dealer.bust:
                    print("딜러가 버스트하여 이기셨습니다")
                    x.money = x.money + (x.bet * 2)
                    print("소지한 금액이 {}으로 되었습니다".format(x.money))
                else:
                    if dealerScore == playerScore:
                        print('비겼습니다')
                        x.money = x.money + x.bet
                        print("소지한 금액이 {}으로 되었습니다".format(x.money))
                    elif dealerScore > playerScore:
                        print('졌습니다')
                        print("소지한 금액이 {}으로 되었습니다".format(x.money))
                    elif dealerScore < playerScore:
                        print("이겼습니다")
                        x.money = x.money + (x.bet * 2)
                        print("소지한 금액이 {}으로 되었습니다".format(x.money))
            
class Card(object):

    def __init__(self, name, num):
        self.name = name
        self.num = num

class Player(object):

    def __init__(self, name, money, cards, bust, bet):
        self.name = name
        self.money = money
        self.cards = cards
        self.bust = bust
        self.bet = bet
        
    def totalScore(self):
        total_score = 0
        ace = False
        for x in self.cards:
            if x.num == 1:
                ace = True
            total_score = total_score + x.num
            if ace:
                if total_score <= 11:
                    total_score = total_score + 10
        return total_score
    
    def showHand(self):
        hand = ""
        for x in self.cards:
            hand = hand + x.name
        return hand
    
    def betting(self):
        print("{}님의 배팅금액을 입력해주세요".format(self.name))
        while True:
            try:
                bet = int(input())
                if bet > self.money:
                    print("소지한 금액보다 큰 돈은 배팅할수없습니다.")
                    error = int("error")
                elif bet <= self.money:
                    self.bet = bet
                    self.money = self.money - bet
                    break
            except:
                print("금액을 입력해주세요")
        
class Dealer(object):

    def __init__(self, cards, bust):
        self.cards = cards
        self.bust = bust
    def giveCard(self, players, cards):
        random.shuffle(cards)
        for y in range(2):
            for x in players:
                x.cards.append(cards[0])
                del cards[0]
            self.cards.append(cards[0])
            del cards[0]
    def totalScore(self):
        total_score = 0
        ace = False
        for x in self.cards:
            total_score = total_score + x.num
            if x.num == 1:
                ace = True
            if ace:
                if total_score <= 11:
                    total_score = total_score + 10
        return total_score
        
    def hit(self, player, cards):
        player.cards.append(cards[0])
        del cards[0]

    def showHand(self):
        hand = ""
        for x in self.cards:
            hand = hand + x.name
        return hand

    def openCard(self, cards):
        while self.totalScore() <= 16:
            self.cards.append(cards[0])
            if self.totalScore() > 21:
                print("딜러는 {}카드를 받았습니다. {}로 21을 넘겼기에 버스트입니다.".format(cards[0].name, self.showHand()))
                self.bust = True
            elif self.totalScore() <= 21:
                print("딜러는 {}카드를 받았습니다. {}입니다.".format(cards[0].name, self.showHand()))
            del cards[0]
            
        
deck = []
player = []

shape = ['♠', '♣', '♥', '◈']
def makeDeck():
        for x in range(1, 14):
            for y in shape:
                
                if x == 1:
                    deck.append(Card("{}A".format(y), x))

                elif x == 11:
                    deck.append(Card("{}J".format(y), 10))
 
                elif x == 12:
                    deck.append(Card("{}Q".format(y), 10))

                elif x == 13:
                    deck.append(Card("{}K".format(y), 10))

                else:
                    deck.append(Card("{}{}".format(y,x), x))

                    
makeDeck()

while True:
    try:
        print("플레이어의 이름을 입력해주세요 (최대 5명이며 띄어쓰기로 구분합니다)")
        member = list(input().split())
        size = len(member)
        if size > 5:
            error = int("에러")
        elif size <= 5:
            break
  
    except:
        print("5명 이하만 입력해주세요")



while True:
    try:
        for x in member:
                print("{}님이 소지한 금액을 입력해주세요".format(x))
                money = int(input())
                player.append(Player(x, money, [], False, 0))
        break

    except:
        print("숫자만 입력해주세요")


game = BlackJack(deck, player, Dealer([], False))
game.gameStart()

