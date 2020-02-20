from abc import ABCMeta, abstractmethod
from enum import IntEnum, unique
from random import shuffle
from collections import Counter

@unique
class Suit(IntEnum):
    hearts = 0
    spades = 1
    clubs = 2
    diamonds = 3

    def symbol(self):
        return '♥♠♣♦'[self.value]


class PlayingCard(metaclass=ABCMeta):
    """
    PlayingCard: Base class for cards
    """

    def __init__(self, suit: Suit):
        self.suit = suit

    @abstractmethod
    def get_value(self):
        pass

    def __eq__(self, other):
        return (self.get_value(), self.suit) == (other.get_value(), self.suit)

    def __lt__(self, other):
        return (self.get_value(), self.suit) < (other.get_value(), self.suit)


class NumberedCard(PlayingCard):
    """
    NumberedCard: A class for the cards with number values (2-10)
    """
    def __init__(self, value, suit):
        super().__init__(suit)
        self.value = value

    def get_value(self):
        return self.value

    def __str__(self):
        return str(self.value) + self.suit.symbol()


class JackCard(PlayingCard):
    """
    JackCard: class to represent a Jack
    """
    def get_value(self):
        return 11

    def __str__(self):
        return 'J' + self.suit.symbol()


class QueenCard(PlayingCard):
    """
    QueenCard: class to represent a Queen
    """
    def get_value(self):
        return 12

    def __str__(self):
        return 'Q' + self.suit.symbol()


class KingCard(PlayingCard):
    """
    KingCard: class to represent a King
    """
    def get_value(self):
        return 13

    def __str__(self):
        return 'K' + self.suit.symbol()


class AceCard(PlayingCard):
    """
    AceCard: class to represent an Ace
    """
    def get_value(self):
        return 14

    def __str__(self):
        return 'A' + self.suit.symbol()


class StandardDeck:
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for value in range(2, 11):
                self.cards.append(NumberedCard(value, suit))
            self.cards.append(JackCard(suit))
            self.cards.append(QueenCard(suit))
            self.cards.append(KingCard(suit))
            self.cards.append(AceCard(suit))

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        shuffle(self.cards)

    def __repr__(self):
        return 'StandardDeck of size {}'.format(len(self.cards))

    def __str__(self):
        return f'[{self.cards[0]}]' + (']' * (len(self.cards) // 10))


class Hand:
    """
    Hand: a class representing the hand of cards for a player
    """
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def sort(self, reverse=False):
        self.cards.sort(reverse=reverse)

    def __str__(self):
        return ', '.join([str(card) for card in self.cards])
    
    def len(self):
        return len(self.cards)

    def best_poker_hand(self, table_cards=None):
        if table_cards is None:
            return PokerHand(self.cards)
        else:
            return PokerHand(self.cards + table_cards)


@unique
class HandType(IntEnum):
    HighCard = 0
    OnePair = 1
    TwoPair = 2
    ThreeOfAKind = 3
    Straight = 4
    Flush = 5
    FullHouse = 6
    FourOfAKind = 7
    StraightFlush = 8


class PokerHand:
    @staticmethod
    def straight_flush(cards):
        """
        Checks for the best straight flush in a list of cards (may be more than just 5)
        :param cards: A list of playing cards.
        :return: None if no straight flush is found, else the value of the top card.
        """
        vals = [(c.get_value(), c.suit) for c in cards] \
            + [(1, c.suit) for c in cards if c.get_value() == 14]  # Add the aces!
        for c in reversed(cards):  # Starting point (high card)
            # Check if we have the value - k in the set of cards:
            found_straight = True
            for k in range(1, 5):
                if (c.get_value() - k, c.suit) not in vals:
                    found_straight = False
                    break
            if found_straight:
                return [c.get_value()]

    @staticmethod
    def straight(cards):
        """
        Checks for the best straight flush in a list of cards (may be more than just 5)
        :param cards: A list of playing cards.
        :return: None if no straight flush is found, else the value of the top card.
        """
        vals = [c.get_value() for c in cards] \
            + [1 for c in cards if c.get_value() == 14]  # Add the aces!
        for c in reversed(cards):  # Starting point (high card)
            # Check if we have the value - k in the set of cards:
            found_straight = True
            for k in range(1, 5):
                if c.get_value() - k not in vals:
                    found_straight = False
                    break
            if found_straight:
                return [c.get_value()]

    @staticmethod
    def flush(cards):
        suit_count = Counter()
        for card in cards:
            suit_count[card.suit] += 1
        # Find the card ranks that have at least three of a kind
        for c in reversed(cards):
            if suit_count[c.suit] >= 5:
                return [c.get_value()]

    @staticmethod
    def full_house(cards):
        """
        Checks for the best full house in a list of cards (may be more than just 5)
        :param cards: A list of playing cards
        :return: None if no full house is found, else a tuple of the values of the triple and pair.
        """
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least three of a kind
        threes = [v[0] for v in value_count.items() if v[1] >= 3]
        threes.sort()
        # Find the card ranks that have at least a pair
        twos = [v[0] for v in value_count.items() if v[1] >= 2]
        twos.sort()

        # Threes are dominant in full house, lets check that value first:
        for three in reversed(threes):
            for two in reversed(twos):
                if two != three:
                    return [three, two]

    @staticmethod
    def two_pairs(cards):
        """
        Checks for the best 2 pairs in a list of cards (may be more than just 5)
        :param cards: A list of playing cards
        :return: None if no 2 pairs are found, else a tuple of the values of the pairs.
        """
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least a pair
        twos = [v[0] for v in value_count.items() if v[1] >= 2]
        twos.sort()

        # Threes are dominant in full house, lets check that value first:
        for two in reversed(twos):
            for second_two in reversed(twos):
                if two != second_two:
                    return [two, second_two]

    @staticmethod
    def four_of_a_kind(cards):
        """
        Checks for the best four of a kind in a list of cards (may be more than just 5)
        :param cards: A list of playing cards
        :return: None if not found, else a list containing the value
        """
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least a pair
        fours = [v[0] for v in value_count.items() if v[1] >= 4]
        fours.sort()

        # Threes are dominant in full house, lets check that value first:
        if fours:
            return [fours[0]]

    @staticmethod
    def three_of_a_kind(cards):
        """
        Checks for the best three of a kind in a list of cards (may be more than just 5)
        :param cards: A list of playing cards
        :return: None if not found, else a list containing the value
        """
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least a pair
        threes = [v[0] for v in value_count.items() if v[1] >= 3]
        threes.sort()

        # Threes are dominant in full house, lets check that value first:
        if threes:
            return [threes[0]]

    @staticmethod
    def one_pair(cards):
        """
        Checks for the best two of a kind in a list of cards (may be more than just 5)
        :param cards: A list of playing cards
        :return: None if not found, else a list containing the value
        """
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least a pair
        twos = [v[0] for v in value_count.items() if v[1] >= 2]
        twos.sort()

        # Threes are dominant in full house, lets check that value first:
        if twos:
            return [twos[0]]

    @staticmethod
    def high_card(cards):
        return [cards[-1].get_value()]

    def __init__(self, cards):
        checks = [PokerHand.straight_flush, PokerHand.four_of_a_kind, PokerHand.full_house,
                  PokerHand.flush, PokerHand.straight, PokerHand.three_of_a_kind,
                  PokerHand.two_pairs, PokerHand.one_pair, PokerHand.high_card]

        for check, htype in zip(checks, reversed(HandType)):
            high_values = check(cards)
            if high_values is not None:
                self.hand_type = htype
                self.high_values = high_values
                break
        else:
            raise ValueError("Couldn't find any matching poker type, not even high card.")

    def __lt__(self, other):
        return (self.hand_type, self.high_values) < (other.hand_type, other.high_values)

    def __eq__(self, other):
        return (self.hand_type, self.high_values) == (other.hand_type, other.high_values)

    def __repr__(self):
        return 'PokerHand(' + self.hand_type.name + ', ' + str(self.high_values) + ')'
