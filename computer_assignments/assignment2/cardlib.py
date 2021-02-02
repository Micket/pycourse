from __future__ import annotations
from abc import ABCMeta, abstractmethod
from enum import IntEnum, unique
from random import shuffle
from typing import List, Dict, Tuple
import numpy as np


@unique
class Suit(IntEnum):
    Hearts = 0
    Spades = 1
    Clubs = 2
    Diamonds = 3


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


class PlayingCard(metaclass=ABCMeta):
    """
    PlayingCard: Base class for cards

    Abstract base class, children need to implement the following methods:
    get_value(self)
    """
    Names = u'♥♠♣♦'

    def __init__(self, suit: Suit):
        """

        :param suit: The cards suit
        :type suit: Suit
        """
        self.suit = suit

    def __repr__(self) -> str:
        return PlayingCard.Names[self.suit] + str(self.get_value())

    def __eq__(self, other: PlayingCard) -> bool:
        return self.suit == other.suit and self.get_value() == other.get_value()

    def __lt__(self, other: PlayingCard) -> bool:
        if self.get_value() == other.get_value():
            return self.suit < other.suit

        return self.get_value() < other.get_value()

    @abstractmethod
    def get_value(self) -> int:
        pass


class NumberedCard(PlayingCard):
    """
    NumberedCard: A class for the cards with number values (2-10)
    """

    def __init__(self, value: int, suit: Suit):
        self.value = value
        super().__init__(suit)

    def get_value(self) -> int:
        return self.value


class JackCard(PlayingCard):
    """
    JackCard: class to represent a Jack
    """

    def __init__(self, suit: Suit):
        super().__init__(suit)

    def get_value(self) -> int:
        return 11

    def __repr__(self) -> str:
        return PlayingCard.Names[self.suit] + 'Jack'


class QueenCard(PlayingCard):
    """
    QueenCard: class to represent a Queen
    """

    def __init__(self, suit: Suit):
        super().__init__(suit)

    def get_value(self) -> int:
        return 12

    def __repr__(self) -> str:
        return PlayingCard.Names[self.suit] + 'Queen'


class KingCard(PlayingCard):
    """
    KingCard: class to represent a King
    """

    def __init__(self, suit: Suit):
        super().__init__(suit)

    def get_value(self) -> int:
        return 13

    def __repr__(self) -> str:
        return PlayingCard.Names[self.suit] + 'King'


class AceCard(PlayingCard):
    """
    AceCard: class to represent an Ace
    """

    def __init__(self, suit: Suit):
        super().__init__(suit)

    def get_value(self) -> int:
        return 14

    def __repr__(self) -> str:
        return PlayingCard.Names[self.suit] + 'Ace'


class StandardDeck(object):
    """
    StandardDeck: A standard deck with 52 cards
    """

    def __init__(self, ordered: bool = True):
        self.cards = list()

        for suit in Suit:
            for value in range(2, 11):
                self.cards.append(NumberedCard(value, suit))

            self.cards.append(JackCard(suit))
            self.cards.append(QueenCard(suit))
            self.cards.append(KingCard(suit))
            self.cards.append(AceCard(suit))

        if not ordered:
            self.shuffle()

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


class PokerHand(object):
    def __init__(self, hand_type: HandType, values: List[int]):
        self.hand_type = hand_type
        self.values = values

    def __lt__(self, other: PokerHand) -> bool:
        return (self.hand_type, self.values) < (other.hand_type, other.values)

    def __eq__(self, other: PokerHand) -> bool:
        return (self.hand_type, self.values) == (other.hand_type, other.values)

    def __repr__(self) -> str:
        return self.hand_type.name + ' ' + str(self.values)


class Hand(object):
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

    def __str__(self) -> str:
        return " ".join(str(c) for c in self.cards)

    def sort(self, reverse=False):
        self.cards.sort(reverse=reverse)

    def count(self) -> int:
        return len(self.cards)

    @staticmethod
    def _is_flush(cards: List[PlayingCard]) -> Tuple[bool, Suit or None]:
        counts = []
        for suit in range(4):
            counts.append(sum([x.suit == suit for x in cards]))

        for i, suit in enumerate(Suit):
            if counts[i] >= 5:
                return True, suit
        return False, None

    @staticmethod
    def _is_straight(card_values: List[int]) -> Tuple[bool, int]:
        count = max_count = 0
        highest_num = 0

        # Build list of unique values (using a set!), add Ace as 14 and 1!
        values = set(card_values)
        if 14 in values:
            values.add(1)
        if 1 in values:
            values.add(14)

        values = sorted(list(values))

        for i in range(1, len(values)):
            if values[i - 1] + 1 == values[i]:
                count += 1
                highest_num = values[i]
            else:
                if count > max_count:
                    max_count = count
                count = 0
                highest_num = 0
            if count > max_count:
                max_count = count

        return max_count + 1 >= 5, highest_num

    @staticmethod
    def _get_counts(cards: List[PlayingCard]) -> Dict[int: List[int]]:
        counts = dict()
        for card in cards:
            if card.get_value() in counts.keys():
                counts[card.get_value()] += 1
            else:
                counts[card.get_value()] = 1
        # Create reverse-dict, i.e. count as key, values as items (in list)
        values = dict()
        for value, count in counts.items():
            if count in values:
                values[count] += [value]
            else:
                values[count] = [value]

        return values

    @staticmethod
    def _filter_out_values(all_values: List[int], filter_values: List[int]) -> List[int]:
        filtered_values = [val for val in all_values if val not in filter_values]
        return filtered_values

    def best_poker_hand(self, cards: List[PlayingCard] = list()) -> PokerHand:
        all_cards = cards.copy()
        all_cards.extend(self.cards)
        all_cards.sort(reverse=True)
        assert len(all_cards) >= 5
        card_values = [c.get_value() for c in all_cards]
        # print(all_cards)

        is_straight, highest_card = self._is_straight(card_values)
        if is_straight:
            cards = [c for c in all_cards if highest_card - 5 < c.get_value() <= highest_card]
            is_flush, _ = self._is_flush(cards)
            if is_flush:
                return PokerHand(HandType.StraightFlush, [cards[0].get_value()])

        is_flush, suit = self._is_flush(all_cards)
        if is_flush:
            vals = [c.get_value() for c in all_cards if c.suit == suit]
            return PokerHand(HandType.Flush, vals[:5])

        if is_straight:
            return PokerHand(HandType.Straight, [cards[0].get_value()])

        # Will return dictionary with count as key, and values for each count in list
        counts = self._get_counts(all_cards)

        if max(counts.keys()) == 4:
            my_values = [sorted(counts[4])[-1]]
            sorted_values = my_values.copy()
            sorted_values.extend(self._filter_out_values(card_values, my_values))
            return PokerHand(HandType.FourOfAKind, sorted_values[:2])

        if max(counts.keys()) == 3:
            my_values = sorted(counts[3])[::-1]

            if len(my_values) < 2 and 2 in counts.keys():
                my_values.append(sorted(counts[2])[-1])

            sorted_values = my_values.copy()
            sorted_values.extend(self._filter_out_values(card_values, my_values))

            if len(my_values) >= 2:
                return PokerHand(HandType.FullHouse, sorted_values[:2])
            else:
                return PokerHand(HandType.ThreeOfAKind, sorted_values[:3])

        if max(counts.keys()) == 2:
            pair_values = sorted(counts[2])[::-1]
            sorted_values = pair_values.copy()
            sorted_values.extend(self._filter_out_values(card_values, pair_values))

            if len(pair_values) >= 2:
                return PokerHand(HandType.TwoPair, sorted_values[:3])
            else:
                return PokerHand(HandType.OnePair, sorted_values[:4])

        return PokerHand(HandType.HighCard, card_values[:5])


class Player:
    """
    Player: A class representing the player
    """

    def __init__(self, name: str, wallet=0):
        self.name = name
        self.wallet = wallet
        self.hand = Hand()
        self.poker_hand = None

    def __str__(self) -> str:
        return 'Player: "{}", Wallet: {}, No. cards: {}'.format(self.name, self.wallet, self.hand.count())

    def add_money(self, amount):
        self.wallet += amount

    def bet(self, amount):
        if amount > self.wallet or amount <= 0:
            raise ValueError

        self.wallet -= amount
        return amount

    def add_cards(self, cards: List[PlayingCard]):
        self.hand.add_cards(cards)

    def find_poker_hand(self, cards: List[PlayingCard] = []):
        self.poker_hand = self.hand.best_poker_hand(cards)


def five_card_draw(no_players: int, rounds: int):
    # Create (shuffled) deck
    deck = StandardDeck(ordered=False)

    # Create players
    players = list()
    for player in range(no_players):
        name = "Player " + str(player + 1)
        players.append(Player(name, 100))

    # Give first hand
    for player in players:
        for _ in range(5):
            player.hand.add_card(deck.draw())
        player.hand.sort()

    for _ in range(rounds):
        print('\n Round :', round)

        for player in players:
            player.hand.sort()
            print(player, '  ', player.hand)

            input_ok = False
            while not input_ok:
                text = input(" comma separated list index of cards to drop (starting from 1, empty for none): ")
                if not text:
                    input_ok = True
                    continue

                try:
                    drops = [int(a) for a in text.split(',')]
                except ValueError:
                    continue

                no_drops = len(drops)

                # Validate input
                input_ok = True
                for i in drops:
                    if not 1 <= i <= 5:
                        input_ok = False
                        break

                drops = np.array(drops) - 1
                player.hand.drop_cards(drops.tolist())
                for _ in range(no_drops):
                    player.hand.add_card(deck.draw())

    print('\nResults:')
    for player in players:
        player.hand.sort()
        print(player, '  ', player.hand)
        player.find_poker_hand()
        print(' Hand:', player.poker_hand)

    print('\nSorted results:')
    for player in sorted(players, key=lambda x: x.poker_hand):
        print(player, '  ', player.hand)
        print(' Hand:', player.hand.best_poker_hand())


def texas_holdem(no_players: int):
    # Create (shuffled) deck
    deck = StandardDeck(ordered=False)

    # Create players
    players = list()
    for player in range(no_players):
        name = "Player " + str(player + 1)
        players.append(Player(name, 100))

    # Give first hand
    for player in players:
        player.add_cards([deck.draw(), deck.draw()])
        player.hand.sort()
        print(player, '  ', player.hand)

    table = Hand()
    for _ in range(3):
        table.add_card(deck.draw())
    print('Table:  ', table, '\n')

    for player in players:
        print(player, end='  ')
        player.find_poker_hand(table.cards)
        print(player.poker_hand)

    for _ in range(2):
        table.add_card(deck.draw())
        print('\nTable:  ', table)

        for player in players:
            print(player, end='  ')
            player.find_poker_hand(table.cards)
            print(player.poker_hand)
        print()

    print('Table:', end='  ')
    table.sort()
    print(table)
    print('\nSorted results:')
    for player in sorted(players, key=lambda x: x.poker_hand):
        print(player, '  ', player.hand)
        print(' PokerHand:', player.poker_hand)


if __name__ == "__main__":

    game_type = 0
    while not 0 < game_type < 3:
        text = input("Choose game type: 1 for 5 card draw, 2 for Texas Hold'em: ")
        try:
            game_type = int(text)
        except ValueError:
            print('"%s" is not an integer!' % text)

    no_players = None
    rounds = 2

    while not isinstance(no_players, int):
        text = input("Enter no. of players: ")
        try:
            no_players = int(text)
        except ValueError:
            print('"%s" is ot an integer!' % text)

    print("No players:", no_players)

    if game_type == 1:
        five_card_draw(no_players, rounds)
    else:
        texas_holdem(no_players)
