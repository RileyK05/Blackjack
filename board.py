def print_game_board(player_chips):
    print("========================================")
    print("             Welcome to Blackjack       ")
    print("========================================\n")
    
    print("Dealer's Hand:")
    print("┌─────────┐  ┌─────────┐")
    print("│░░░░░░░░░│  │░░░░░░░░░│")
    print("│░ BLACK ░│  │░ JACK  ░│")
    print("│░░░░░░░░░│  │░░░░░░░░░│")
    print("└─────────┘  └─────────┘\n")
    
    print("Player's Hand:")
    print("┌─────────┐  ┌─────────┐")
    print("│         │  │         │")
    print("│         │  │         │")
    print("│         │  │         │")
    print("└─────────┘  └─────────┘\n")
    
    print(f"Your Chips: {player_chips}")
    print("========================================")