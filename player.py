class Player:
    def __init__(self):
        self.hand = []
        self.chips = 100
        
    def add_card(self, card):
        self.hand.append(card)