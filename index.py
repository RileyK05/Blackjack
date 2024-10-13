import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.assign_value()
        
    def assign_value(self):
        if self.rank == 'Ace':
            return 11
        if self.rank in ['King', 'Queen', 'Jack']:
            return 10
        else:
            return int(self.rank) 
        
    def __str__(self):
        return self.rank + " of " + self.suit
        
class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()
        
    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop() if len(self.cards) > 0 else None
        
    def __str__(self):
        return ', '.join([str(card) for card in self.cards])
    
class Player:
    def __init__(self):
        self.hand = []
        self.chips = 100
        
    def add_card(self, card):
        self.hand.append(card)
        
        
def main():
    deck = Deck()
    game_state = False
    
    print("To start game, press 1")
    print("To quit game, press 2")
    usr_start = input("Enter: ")
    
    if usr_start == 1:
        game_state = True
    else:
        print("Ended")
        
    while game_state:
        
    



if __name__ == "__main__":
    main()
