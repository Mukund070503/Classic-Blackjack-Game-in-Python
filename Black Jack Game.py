from random import shuffle

cards = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
card_value = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

# Card class
class Card():
    def __init__(self, card, suit):
        self.card = card
        self.suit = suit

    def __str__(self):
        return f"{self.card} of {self.suit}"

# Deck class
class Deck():
    no_of_cards = 0
    cards_in_deck = []

    def __init__(self):
        pass

    @classmethod
    def add_card(cls, card):
        cls.no_of_cards += 1
        cls.cards_in_deck.append(card)

    @classmethod
    def shuffle_deck(cls):
        shuffle(cls.cards_in_deck)

    @classmethod
    def remove_card(cls):
        if cls.cards_in_deck:  # Check to prevent popping from an empty list
            return cls.cards_in_deck.pop(0)
        return None

    def __str__(cls):
        return f"Deck has {cls.no_of_cards} cards"

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.mycards = []
        self.bet = [0]
        self.amount = 0
        self.sum = 0

    def pick_cards(self):
        card = Deck.remove_card()
        if card:
            self.mycards.append(card)

    def place_bet(self, amount):
        self.amount = 0
        self.bet.append(amount)
        for amount in self.bet:
            self.amount += amount
        print(f"Now, the total bet amount is {self.amount}")

    def total_of_cards(self):
        self.sum = 0
        for card in self.mycards:
            self.sum += card_value[card.card]
        return self.sum

    def __str__(self):
        if self.name == "Dealer":
            return f"Hi, {self.name} here"
        else:
            return f"Hi, {self.name} here. The value of my cards is {self.total_of_cards()} and the amount I bet is {self.amount}"

# Completing the Deck with cards
for suit in suits:
    for card in cards:
        value = Card(card, suit)
        Deck.add_card(value)

# Shuffle the cards in the deck
print(Deck())
Deck.shuffle_deck()

# Complete game logic
print("Hi, welcome to the Black Jack Game")
Comp = Player("Dealer")  # Corrected 'player' to 'Player'
print(Comp)
player_name = input("Enter your name:")  # Changed 'Player' to 'player_name' to avoid confusion
Player1 = Player(player_name)  # Corrected 'player' to 'Player'
game_on = True
round = 0
while game_on:
    if Comp.total_of_cards() > 21 and Player1.total_of_cards() > 21:
        print("It's a tie!")
        game_on = False
        break
    elif Comp.total_of_cards() > 21:
        print("Dealer burst! You WON!")
        game_on = False
        break
    elif Player1.total_of_cards() > 21:
        print("You lost 😢")
        game_on = False
        break
    if round == 0:
        amount = int(input("Enter the amount to bet:"))
        Player1.place_bet(amount)
        Player1.pick_cards()
        Player1.pick_cards()
        print(f"The total of cards for Player1 is {Player1.total_of_cards()}")
        Comp.pick_cards()
        Comp.pick_cards()
        print(f"The open card of Dealer is {Comp.mycards[0]}")
        round += 1
    else:
        bet_check = input("Do you want to bet more? (Answer in Yes or No): ")
        if bet_check == "Yes":
            amount = int(input("Enter the amount you want to include to bet: "))
            Player1.place_bet(amount)

        choice = input("Do you want to HIT or STAND? ")
        if choice == "HIT":
            Player1.pick_cards()
            print(f"The total of cards for Player1 is {Player1.total_of_cards()}")
            Comp.pick_cards()
            print(f"The total of cards for Dealer is {Comp.total_of_cards()}")
        else:
            pass
