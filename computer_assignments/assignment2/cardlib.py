from __future__ import annotations

from abc import ABCMeta, abstractmethod
from enum import IntEnum, unique
from random import shuffle
from typing import List, Dict, Tuple
from collections import Counter, defaultdict

import numpy as np


@unique
class Suit(IntEnum):
    Hearts = 0
    Spades = 1
    Clubs = 2
    Diamonds = 3

    def symbol(self):
        return '♥♠♣♦'[self.value]


@unique
class PokerType(IntEnum):
    HighCard = 0
    OnePair = 1
    TwoPair = 2
    ThreeOfAKind = 3
    Straight = 4
    Flush = 5
    FullHouse = 6
    FourOfAKind = 7
    StraightFlush = 8


class PlayingCard(metaclass=ABCMeta):
    """
    PlayingCard: Base class for cards

    Abstract base class, children need to implement the following methods:
    get_value(self)
    """

    def __init__(self, suit: Suit):
        """
        :param suit: The cards suit
        """
        self.suit = suit

    def __eq__(self, other: PlayingCard) -> bool:
        return self.suit == other.suit and self.get_value() == other.get_value()

    def __lt__(self, other: PlayingCard) -> bool:
        return (self.get_value(), self.suit) < (other.get_value(), other.suit)

    @abstractmethod
    def get_value(self) -> int:
        pass


class NumberedCard(PlayingCard):
    """
    NumberedCard: A class for the cards with number values (2-10)
    """

    def __init__(self, value: int, suit: Suit):
        super().__init__(suit)
        self.value = value

    def get_value(self) -> int:
        return self.value

    def __str__(self) -> str:
        return f'{self.value}{self.suit.symbol()}'


class JackCard(PlayingCard):
    """
    JackCard: class to represent a Jack
    """
    def get_value(self) -> int:
        return 11

    def __str__(self) -> str:
        return f'J{self.suit.symbol()}'


class QueenCard(PlayingCard):
    """
    QueenCard: class to represent a Queen
    """
    def get_value(self) -> int:
        return 12

    def __str__(self) -> str:
        return f'Q{self.suit.symbol()}'


class KingCard(PlayingCard):
    """
    KingCard: class to represent a King
    """
    def get_value(self) -> int:
        return 13

    def __str__(self) -> str:
        return f'K{self.suit.symbol()}'


class AceCard(PlayingCard):
    """
    AceCard: class to represent an Ace
    """
    def get_value(self) -> int:
        return 14

    def __str__(self) -> str:
        return f'A{self.suit.symbol()}'


class StandardDeck:
    """
    StandardDeck: A standard deck with 52 cards
    """
    def __init__(self):
        self.cards = []

        for suit in Suit:
            for value in range(2, 11):
                self.cards.append(NumberedCard(value, suit))
            for ctor in [JackCard, QueenCard, KingCard, AceCard]:
                self.cards.append(ctor(suit))


    def shuffle(self):
        """
        Random shuffle of deck
        :return:
        """
        shuffle(self.cards)

    def sort(self, reverse: bool = False):
        self.cards.sort(reverse=reverse)

    def draw(self) -> PlayingCard:
        """
        Draws a card from the deck

        :return: The card drawn
        """
        return self.cards.pop()


class PokerHand:
    @staticmethod
    def check_high_card(cards):
        return max(v.get_value() for v in cards)

    @staticmethod
    def check_pair(cards):
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least a pair
        twos = [v[0] for v in value_count.items() if v[1] >= 2]
        if twos:
            return max(twos)

    @staticmethod
    def check_two_pair(cards):
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least a pair
        twos = [v[0] for v in value_count.items() if v[1] >= 2]
    
        if len(twos) >= 2:
            twos.sort(reverse=True)
            return twos[:2]

    @staticmethod
    def check_three_of_a_kind(cards):
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least 3
        threes = [v[0] for v in value_count.items() if v[1] >= 3]
        if threes:
            return max(threes)

    @staticmethod
    def check_straight(cards):
        vals = [c.get_value() for c in cards] \
            + [1 for c in cards if c.get_value() == 14]  # Add the aces!
        for c in reversed(cards): # Starting point (high card)
            # Check if we have the value - k in the set of cards:
            found_straight = True
            for k in range(1, 5):
                if (c.get_value() - k) not in vals:
                    found_straight = False
                    break
            if found_straight:
                return c.get_value()

    @staticmethod
    def check_flush(cards):
        """
        Checks for the best full house in a list of cards (may be more than just 5)
    
        :param cards: A list of playing cards
        :return: None if no flush is found, else highest 5 values of flush
        """
    
        # Needlessly general for conventional poker games:
        # this makes no assumptions on the total number of cards
        by_suit = defaultdict(list)
        for c in cards:
            by_suit[c.suit].append(c.get_value())
    
        best_values = [0]
        for values in by_suit.values():
            if len(cards) >= 5 and max(values) > max(best_values):
                best_values = values
        if max(best_values) > 0:
            return best_values[:5]

    @staticmethod
    def check_full_house(cards):
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least three of a kind
        threes = [v[0] for v in value_count.items() if v[1] >= 3]
        threes.sort(reverse=True)
        # Find the card ranks that have at least a pair
        twos = [v[0] for v in value_count.items() if v[1] >= 2]
        twos.sort(reverse=True)
    
        # Threes are dominant in full house, lets check that value first:
        for three in threes:
            for two in twos:
                if two != three:
                    return three, two

    @staticmethod
    def check_four_of_a_kind(cards):
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least 4
        fours = [v[0] for v in value_count.items() if v[1] >= 4]
        if fours:
            return max(fours)

    @staticmethod
    def check_straight_flush(cards):
        vals = [(c.get_value(), c.suit) for c in cards] \
            + [(1, c.suit) for c in cards if c.get_value() == 14]  # Add the aces!
        for c in reversed(cards): # Starting point (high card)
            # Check if we have the value - k in the set of cards:
            found_straight = True
            for k in range(1, 5):
                if (c.get_value() - k, c.suit) not in vals:
                    found_straight = False
                    break
            if found_straight:
                return c.get_value()

    def __init__(self, cards: List[PlayingCard]):
        assert len(cards) >= 5

        checks = [
            self.check_straight_flush,
            self.check_four_of_a_kind,
            self.check_full_house,
            self.check_flush,
            self.check_straight,
            self.check_three_of_a_kind,
            self.check_two_pair,
            self.check_pair,
            self.check_high_card,
        ]

        cards.sort(reverse=True)
        for check, ptype in zip(checks, reversed(PokerType)):
            values = check(cards)
            if values is not None:
                self.values = values
                self.poker_type = ptype
                break

    def __lt__(self, other: PokerHand) -> bool:
        return (self.poker_type, self.values) < (other.poker_type, other.values)

    def __eq__(self, other: PokerHand) -> bool:
        return (self.poker_type, self.values) == (other.poker_type, other.values)

    def __repr__(self) -> str:
        return f'PokerHand({self.poker_type}, {self.values})'


class Hand:
    """
    Hand: a class representing the hand of cards for a player
    """

    def __init__(self):
        self.cards = []

    def add_cards(self, cards: List[PlayingCard] or PlayingCard):
        if not isinstance(cards, list):
            self.cards.append(cards)
        else:
            self.cards.extend(cards)

    def add_card(self, card: PlayingCard):
        self.cards.append(card)

    def drop_cards(self, indices: List[int]):
        assert len(indices) <= len(self.cards)

        indices.sort(reverse=True)
        for i in indices:
            self.cards.pop(i)

    def best_poker_hand(self, cards: List[PlayingCard] = []) -> PokerHand:
        return PokerHand(self.cards + cards)

    def __str__(self) -> str:
        return " ".join(str(c) for c in self.cards)

    def sort(self, reverse=False):
        self.cards.sort(reverse=reverse)

    def count(self) -> int:
        return len(self.cards)

