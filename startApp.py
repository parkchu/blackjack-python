from BlackJack import BlackJack
from Dealer import Dealer
from Deck import *

deck = makeDeck()
dealer = Dealer([], deck)
players = []
blackJack = BlackJack(dealer, players)
blackJack.readyGame()

while True:
    blackJack.gameStart()
