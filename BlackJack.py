import time
import random
from Dealer import Dealer
from Player import Player
from Deck import *

class BlackJack(object):
    def __init__(self, dealer, player):
        self.dealer = dealer
        self.player = player
        
    def playerNum(self):
        player_num = int(input())
        return player_num

    def getNameMoney(self, player_num):
        for x in range(player_num):
            name_money = list(input().split())
            name = name_money[0]
            money = int(name_money[1])
            player = Player(name, money, [], 0)
            self.player.append(player)

    def hasAce(self, someone):
        for x in someone.hand:
            if x.num == 1:
                return True
        return False
            
    def totalScore(self, someone):
        total_score = 0
        for x in someone.hand:
            total_score += x.num
        if self.hasAce(someone):
            if total_score + 10 <= 21:
                total_score += 10
            return total_score
        
        else:
            return total_score

    def whetherBust(self, someone):
        total_score = self.totalScore(someone)
        if total_score > 21:
            return True
            
        elif total_score <= 21:
            return False

    def resultDealer(self):
        dealer_total_score = self.totalScore(self.dealer)
        if self.dealer.whetherGetCard(dealer_total_score):
            self.dealer.getCard()
            if self.dealer.whetherGetCard(self.totalScore(self.dealer)):
                return False
            else:
                return True
        else:
            return True

    def result(self, player):
        p_total_score = self.totalScore(player)
        dealer_total_score = self.totalScore(self.dealer)
        if self.whetherBust(player):
            return "playerBust"
        else:
            if self.whetherBust(self.dealer):
                player.win()
                return "dealerBust"
            else:
                if p_total_score == dealer_total_score:
                    player.draw()
                    return "draw"
                elif p_total_score > dealer_total_score:
                    player.win()
                    return "playerWin"
                elif p_total_score < dealer_total_score:
                    return "dealerWin"
                    
    def readyGame(self):
        print("몇명의 플레이어가 참여합니까? (최대 5명)")
        player_num = self.playerNum()
        print("플레이어의 이름과 보유중인 금액을 입력해주세요. (띄어쓰기로 구분합니다)")
        self.getNameMoney(player_num)
        
    def gameStart(self):
        time.sleep(0.5)
        print("게임을 시작하도록 하겠습니다")
        for x in self.player:
            time.sleep(1)
            print("{}님의 보유 금액은 {}입니다. 배팅해주세요".format(x.name, x.money))
            while True:
                try:
                    x.betting()
                    break
                except:
                    print("배팅금액만큼의 돈을 소유하고 계시지 않습니다 다시 입력해주세요")
        self.dealer.gameStart(self.player)
        time.sleep(1)
        print("딜러의 카드: " + self.dealer.hand[0].name)
        for x in self.player:
            while True:
                time.sleep(1)
                print("{}님의 카드: ".format(x.name) + x.showHand(), self.totalScore(x))
                time.sleep(0.5)
                print("카드를 더 받으시겠습니까? (hit or stay)")
                if x.whetherHit():
                    self.dealer.playerGetCard(x)
                    print("받으신 카드: " + x.hand[-1].name)
                    time.sleep(1)
                    if self.whetherBust(x):
                        print("{}님은 카드의 합이 21을 넘기셔서 버스트 하셨습니다".format(x.name), self.totalScore(x))
                        break
                else:
                    break
        print("딜러의 카드: " + self.dealer.showHand(), self.totalScore(self.dealer))
        while True:
            time.sleep(1)
            boolean = self.resultDealer()
            if boolean:
                if len(self.dealer.hand) == 2:
                    break
                else:
                    print("딜러의 카드: " + self.dealer.showHand(), self.totalScore(self.dealer))
                    break
            else:
                print("딜러의 카드: " + self.dealer.showHand(), self.totalScore(self.dealer))

        for x in self.player:
            result = self.result(x)
            time.sleep(1)
            if result == "playerBust":
                print("{}님은 버스트했습니다".format(x.name))
            elif result == "dealerBust":
                print("{}님은 딜러가 버스트하여 승리하셨습니다".format(x.name))
            elif result == "draw":
                print("{}님은 무승부 입니다".format(x.name))
            elif result == "playerWin":
                print("{}님은 이기셨습니다".format(x.name))
            elif result == "dealerWin":
                print("{}님은 패배하셨습니다".format(x.name))
            x.resetHand()
        self.dealer.resetHand()
        
                    
            





        
