"""
Author: Alex Birchfield
Description: blackjack card came using OOP
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen',
         'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank).__str__()
                self.deck.append(card)

    def get_list(self):
        return ", ".join(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        for key in values:
            if key in card:
                self.value += values[key]

    def get_list(self):
        return ", ".join(self.cards)

    def adjust_for_ace(self):
        for card in self.cards:
            if "Ace" in card:
                self.aces += 1


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def loose_bet(self):
        self.total -= self.bet


def take_bet(player):
    waiting = True
    while waiting:
        try:
            amount = int(input("Enter amount you want to bet: "))
        except ValueError:
            print("ERROR! Please enter an integer: ")
        else:
            if amount > player.total:
                print("ERROR! Your bet goes over the amount of total chips you have")
                continue
            waiting= False
    print("")
    return amount


def hit(deck, hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    keep_hitting = True
    while keep_hitting:
        move = input("Do you want to hit or stay? ").lower()
        while move != 'hit' and move != 'stay':
            print("ERROR! Must type 'hit' or 'stay'!")
            move = input("Do you want to hit or stay? ").lower()
        if move == 'hit':
            hit(deck, hand)
            hand.adjust_for_ace()

            if hand.value > 21:
                if hand.aces > 0:
                    hand.value -= 10 * hand.aces
                    hand.aces = -5  # So it doesnt keep subtracting 10 after it accounts for it once
                else:
                    break
            print(f"{hand.get_list()} which is {hand.value} points")
        else:
            keep_hitting = False


def show_some(player, dealer):
    print(f"Player's cards: {player.get_list()}")
    dealer_hand = dealer.get_list().split(',')
    print(f"Dealer's cards: {dealer_hand[1]}\n")


def show_all(player, dealer):
    print(f"Player's cards: {player.get_list()}")
    print(f"Player's total value: {player.value}")
    print(f"Dealer's cards: {dealer.get_list()}")
    print(f"Dealer's total value: {dealer.value}")


def player_busts(chips):
    print("Your hand went over 21! You lose!")
    chips.loose_bet()


def player_21(chips):
    print("Blackjack! You hit 21 points!")
    chips.win_bet()


def player_wins(chips):
    print("Congrats! You won the hand!")
    chips.win_bet()


def dealer_busts(chips):
    print("The dealer went over 21. You win the hand!")
    chips.bet = chips.bet * 1.5
    chips.win_bet()


def dealer_wins(chips):
    print("Dealer won the hand. You lose!")
    chips.loose_bet()


def push():
    print("You and the dealer have the same total value. You neither win or lose chips")


def replay():
    result = input("Play again? ").lower()
    while result != 'yes' and result != 'no':
        print("ERROR! Must answer 'yes' or 'no'")
        result = input("Play again? ").lower()
    return result


player_chips = Chips()


while True:
    print("Welcome to Python Blackjack\n")

    card_deck = Deck()
    card_deck.shuffle()

    player = Hand()
    dealer = Hand()

    player.add_card(card_deck.deal())
    dealer.add_card(card_deck.deal())
    player.add_card(card_deck.deal())
    dealer.add_card(card_deck.deal())

    if player_chips.total <= 0:
        print("You have no more chips left! Goodbye!")
        break
    print(f"You have {player_chips.total} chips")
    player_chips.bet = take_bet(player_chips)

    show_some(player, dealer)

    playing = True

    while True:
        hit_or_stand(card_deck, player)
        if player.value > 21:
            show_all(player, dealer)
            player_busts(player_chips)
            break
        if player.value == 21:
            show_all(player, dealer)
            player_21(player_chips)
            player_chips.total += player_chips.bet * .5
            break
        show_all(player, dealer)
        while dealer.value < 17:
            dealer.add_card(card_deck.deal())
            show_all(player, dealer)
        if dealer.value > 21:
            dealer_busts(player_chips)
            break
        elif player.value > dealer.value:
            player_wins(player_chips)
            break
        elif player.value < dealer.value:
            dealer_wins(player_chips)
            break
        else:
            push()
            break

    again = replay()
    if again == 'yes':
        continue
    else:
        print("Goodbye!")
        break
