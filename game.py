import random
from player import Player
from board import print_game_board
from deck import Deck
from game import GameState

class GameState:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()
        self.pot = 0