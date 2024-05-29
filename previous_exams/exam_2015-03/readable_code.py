# This is the file to convert:

from random import shuffle


class NumberedCard:
    """
    Some class 
    """
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def give_value(self):
        return self.value

    def __str__(self):
        return str(self.value) + str(self.suit)


class StandardDeck:
    """
    Another class
    """
    def __init__(self):
        self.cards = [1, 2, 3] # ( this code is Left out in this example file )

    def shuffle(self):
        shuffle(self.cards)

    def give_card(self):
        return self.cards.pop(-1)

    def __str__(self):
        return "Deck: " + ', '.join(self.cards)


class Hand:
    """
    Class för en hand med kort
    """
    def __init__(self):
        self.cards = []

    @staticmethod
    def check_pair(cards):
        """
        Support function for checking of a pair exists
        """
        value_count = Counter()
        for c in cards:
            value_count[c.value] += 1
        twos = [v[0] for v in value_count.items() if v[1] >= 2]
        twos.sort()
        if len(twos) > 1:
            return twos[-1]

    def clear_cards(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return "Hand has: " + ', '.join(self.cards)
