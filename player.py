class Player:
    def __init__(self):
        self.hand = []
        self.chips = 100

    def add_card(self, card):
        self.hand.append(card)

    def hand_value(self):
        value = sum(card.value for card in self.hand)
        aces = sum(1 for card in self.hand if card.rank == 'Ace')
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
