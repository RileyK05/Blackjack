def print_game_board(player_chips, player_hand=None, dealer_hand=None, hide_dealer_card=True):
    print("\n========================================")
    print("             Welcome to Blackjack       ")
    print("========================================")
    print(f"Your Chips: {player_chips}\n")

    print("Dealer's Hand:")
    if dealer_hand:
        dealer_cards = []
        for i, card in enumerate(dealer_hand):
            if i == 0 and hide_dealer_card:
                dealer_cards.append("Hidden Card")
            else:
                dealer_cards.append(str(card))
        print(', '.join(dealer_cards))
    else:
        print("No cards yet.")

    print("\nYour Hand:")
    if player_hand:
        print(', '.join(str(card) for card in player_hand))
        print(f"Hand Value: {sum(card.value for card in player_hand)}")
    else:
        print("No cards yet.")
    print("========================================\n")
