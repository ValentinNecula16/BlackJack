import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_cards = []
computer_cards = []

user_cards.append(deal_card())
user_cards.append(deal_card())

computer_cards.append(deal_card())
computer_cards.append(deal_card())

print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
print(f"Dealer's first card: {computer_cards[0]}")

game_over = False

while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        cont = input("Type 'Y' to get another card, type 'N' to pass: ").upper()
        if cont == "Y":
            user_cards.append(deal_card())
        else:
            game_over = True

while calculate_score(computer_cards) < 17:
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"\nYour final hand: {user_cards}, final score: {user_score}")
print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")

if user_score > 21:
    print("You went over. You lose 😵")
elif computer_score > 21:
    print("Dealer went over. You win! 🥳")
elif user_score == computer_score:
    print("Draw! 🙃")
elif user_score == 0:
    print("Blackjack! You win! 🃏🎉")
elif computer_score == 0:
    print("Dealer has Blackjack. You lose 😭")
elif user_score > computer_score:
    print("You win! 🔥")
else:
    print("You lose 😞")
