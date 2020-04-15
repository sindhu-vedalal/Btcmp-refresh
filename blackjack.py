"""
To play a hand of Blackjack the following steps must be followed:

1. Create a deck of 52 cards
2. Shuffle the deck
3. Ask the Player for their bet
4. Make sure that the Player's bet does not exceed their available chips
5. Deal two cards to the Dealer and two cards to the Player
6. Show only one of the Dealer's cards, the other remains hidden
7. Show both of the Player's cards
8. Ask the Player if they wish to Hit, and take another card
9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10. If a Player Stands, play the Dealer's hand.
     The dealer will always Hit until the Dealer's value meets or exceeds 17
11. Determine the winner and adjust the Player's chips accordingly
12. Ask the Player if they'd like to play again
"""
import random


class Card:
    """
    Card class made of card number and value
    """
    def __init__(self, value, shape):
        """

        :param value: card value i.e., Ace to KIng
        :type value: int
        :param shape: Card shape
        :type shape: str
        """
        self.value = value
        self.shape = shape

    def get_value(self):
        """

        :return: Value of card, value is 10 for face card
        :rtype:
        """
        return self.value if self.value in range(1, 10) else 10

    def get_shape(self):
        """

        :return: shape i.e., heard, spade, etc..
        :rtype: str
        """
        return self.shape

    def __str__(self):
        """

        :return: string
        :rtype: str
        """
        return self.shape + " " + str(self.value)


class BlackJack:
    """
    BlackJack players with methods
    """
    def __init__(self, bet=5000):
        """

        :param bet: bet amount
        :type bet: int
        """
        self.score = 0
        self.bet = bet

    def new_card(self, dck, score=0):
        """

        :param dck: deck of cards
        :type dck: Card list
        :param score: score of player/dealer
        :type score: int
        :return: Card score n shape
        :rtype: str
        """
        crd = dck.pop()
        print("Score of card dealt: ", crd.get_value())
        self.score = score + crd.get_value()
        print("Total SCore: ", self.score)
        return str(crd.get_value()) + " " + crd.get_shape()

    def bet_set(self, amount=0):
        """

        :param amount:
        :type amount:
        :return: if there are sufficient chips
        :rtype: int or str
        """
        return self.bet - amount if amount <= self.bet else "Insufficient amount"

    def bust_check(self):
        """

        :return: BUST if > 21
        :rtype: str
        """
        print("SCORE IN BUST CHECK: {}".format(self.score))
        return "BUST" if self.score >= 21 else "NOPE"


def game(playr, dealr, dck):
    """

    :param playr: player
    :type playr: BlackJack
    :param dealr: card dealer
    :type dealr: BlackJack
    :param dck: card deck
    :type dck: Card list
    :return: None
    :rtype: None
    """
    bet = 0
    while True:
        bet = int(input("Enter bet amount: "))
        if playr.bet_set() == "Insufficient amount":
            print("You need to enter an amount below {}".format(playr.bet_set))
        else:
            break

    print("Dealing first card to player")
    print(playr.new_card(dck))
    print("PLAYER SCORE = {}".format(playr.score))
    print("Dealing 2nd card to player ")
    print(playr.new_card(dck, playr.score))
    print("PLAYER SCORE = {}".format(playr.score))
    print("Dealing 1st card to dealer")
    print(dealr.new_card(dck))
    print("DEALER SCORE: {}".format(dealr.score))
    print("Dealing 2nd card to dealer (not revealing card)")
    # print(dealer.new_card(deck, dealer.score))
    dealr.new_card(dck, dealr.score)
    while input("So player, would you like to hit and take another \
     card ?(Yes/No) : ").casefold() == "Yes":
        print("Dealing to PLayer")
        print(playr.new_card(dck, playr.score))
        print("PLAYER SCORE = {}".format(playr.score))
        if playr.bust_check() == "BUST":
            print("OH NO! BUSTED! Better luck next time")
            print("YOu have {} chips left".format(playr.bet_set(bet)))
            return None

    while dealr.score <= 17:
        print("Dealing dealer")
        dealr.new_card(dck, dealr.score)
        print("DEALER SCORE: {}".format(dealr.score))

    print("Let see the results!")

    if playr.score > dealr.score or dealr.bust_check() == "BUST":
        print("CONGRATULATIONS! YOU WON")
        print("YOu have {} chips now!".format(playr.bet_set(-bet)))
    else:
        print("OH no! Better luck next time!")
        print("YOu have {} chips left".format(playr.bet_set(bet)))


if __name__ == "__main__":
    print("WELCOME TO BLACKJACK")
    print("")
    CARD_SH = ["heart", "diamond", "clubs", "spade"]
    DECK = [Card(value, shape) for value in range(1, 14) for shape in CARD_SH]
    random.shuffle(DECK)
    PLAYER = BlackJack()
    print("Created PLAYER")
    DEALER = BlackJack(0)
    print("Created DEALER")
    game(PLAYER, DEALER, DECK)
    while PLAYER.bet_set() != "Insufficient amount":
        if input("Would you like to play again?: ") == "Yes":
            game(PLAYER, DEALER, DECK)
        else:
            break

    print("Thank you for playing! Come again some time! :)")
