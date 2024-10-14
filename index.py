import random
from player import Player
from board import print_game_board
from deck import Deck
from game import GameState
     
def main():
    deck = Deck()
    game_state = False
    
    print("To start game, press 1")
    print("To quit game, press 2")
    usr_start = int(input("Enter: "))
    
    if usr_start == 1:
        game_state = True
        player = Player()
        print_game_board(player.chips)
    else:
        print("Ended or poor input")
        
    while game_state:
        usr_chip_bet = int(input("How many chips to bargain: "))
        player.chips -= usr_chip_bet
        


if __name__ == "__main__":
    main()
