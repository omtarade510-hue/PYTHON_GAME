import random

# Card values
cards = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 11, "Q": 12, "K": 13, "A": 14
}

card_list = list(cards.keys())

player_score = 0
computer_score = 0

rounds = 5

print("🃏 Welcome to High Card Game!")
print("Best of 5 rounds wins.\n")

for i in range(rounds):
    input(f"Press Enter to draw card for Round {i+1}...")

    player_card = random.choice(card_list)
    computer_card = random.choice(card_list)

    print("You drew:", player_card)
    print("Computer drew:", computer_card)

    if cards[player_card] > cards[computer_card]:
        print("You win this round!\n")
        player_score += 1
    elif cards[player_card] < cards[computer_card]:
        print("Computer wins this round!\n")
        computer_score += 1
    else:
        print("It's a tie!\n")

print("Final Score:")
print("You:", player_score)
print("Computer:", computer_score)

if player_score > computer_score:
    print("🎉 Congratulations! You won the game!")
elif player_score < computer_score:
    print("😢 Computer won the game!")
else:
    print("🤝 The game is a draw!")