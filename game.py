from deck import Deck
from player import Player
from board import print_game_board

class GameState:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()
        self.pot = 0
        self.game_over = False

    def start_game(self):
        while True:
            print("To start game, press 1")
            print("To quit game, press 2")
            usr_start = input("Enter: ").strip()
            if usr_start == '1':
                self.game_over = False
                print_game_board(self.player.chips)
                self.play_game()
                break
            elif usr_start == '2':
                print("Game ended.")
                self.game_over = True
                break
            else:
                print("Invalid input. Please enter 1 or 2.")

    def play_game(self):
        while not self.game_over:
            while True:
                usr_chip_bet = input("How many chips to wager: ").strip()
                if not usr_chip_bet.isdigit():
                    print("Invalid input. Please enter a positive integer.")
                    continue
                usr_chip_bet = int(usr_chip_bet)
                if usr_chip_bet <= 0:
                    print("Bet must be a positive integer.")
                elif usr_chip_bet > self.player.chips:
                    print("You don't have enough chips!")
                else:
                    break
            self.player.chips -= usr_chip_bet
            self.pot += usr_chip_bet * 2

            self.deal_initial_cards()
            self.player_turn()
            self.dealer_turn()
            self.determine_winner()
            self.reset_round()

    def deal_initial_cards(self):
        self.player.hand = [self.deck.deal(), self.deck.deal()]
        self.dealer.hand = [self.deck.deal(), self.deck.deal()]
        print_game_board(self.player.chips, self.player.hand, self.dealer.hand, hide_dealer_card=True)

    def player_turn(self):
        while True:
            choice = input("Do you want to 'hit' or 'stand'? ").strip().lower()
            if choice == 'hit':
                card = self.deck.deal()
                self.player.add_card(card)
                print(f"You drew {card}.")
                if self.player.hand_value() > 21:
                    print("You busted!")
                    break
                print_game_board(self.player.chips, self.player.hand, self.dealer.hand, hide_dealer_card=True)
            elif choice == 'stand':
                break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")

    def dealer_turn(self):
        while self.dealer.hand_value() < 17:
            card = self.deck.deal()
            self.dealer.add_card(card)
            print(f"Dealer draws {card}.")

    def determine_winner(self):
        player_value = self.player.hand_value()
        dealer_value = self.dealer.hand_value()
        print_game_board(self.player.chips, self.player.hand, self.dealer.hand, hide_dealer_card=False)
        if player_value > 21:
            print("Dealer wins!")
        elif dealer_value > 21 or player_value > dealer_value:
            print("You win!")
            self.player.chips += self.pot
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")
            self.player.chips += self.pot // 2
        self.pot = 0

    def reset_round(self):
        self.player.hand.clear()
        self.dealer.hand.clear()
        if self.player.chips <= 0:
            print("You're out of chips! Game over.")
            self.game_over = True
        else:
            while True:
                play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
                if play_again == 'yes':
                    break
                elif play_again == 'no':
                    self.game_over = True
                    print("Thank you for playing!")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
