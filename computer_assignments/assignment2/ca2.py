from abc import ABCMeta, abstractmethod
from enum import IntEnum, unique
import numpy as np


@unique
class Suit(IntEnum):
    hearts = 0
    spades = 1
    clubs = 2
    diamonds = 3


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
    give_value(self)
    """
    Names = u'♥♠♣♦'

    def __init__(self, value, suit, lowest=1, highest=14):
        self.suit = suit
        if not lowest <= value <= highest:
            raise ValueError
        self.value = value

    def __repr__(self):
        return PlayingCard.Names[self.suit] + str(self.value)

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def __lt__(self, other):
        if self.value == other.value:
            return self.suit < other.suit

        return self.value < other.value

    # @abstractmethod
    def give_value(self):
        return self.value

    def same_value(self, other):
        return self.value == other.value

    def same_suit(self, other):
        return self.suit == other.suit


class NumberedCard(PlayingCard):
    """
    NumberedCard: A class for the cards with number values (2-10)
    """

    def __init__(self, value, suit):
        super().__init__(value, suit, lowest=2, highest=10)


class JackCard(PlayingCard):
    """
    JackCard: class to represent a Jack
    """

    def __init__(self, suit):
        super().__init__(11, suit)

    def __repr__(self):
        return PlayingCard.Names[self.suit] + 'Jack'


class QueenCard(PlayingCard):
    """
    QueenCard: class to represent a Queen
    """

    def __init__(self, suit):
        super().__init__(12, suit)

    def __repr__(self):
        return PlayingCard.Names[self.suit] + 'Queen'


class KingCard(PlayingCard):
    """
    KingCard: class to represent a King
    """

    def __init__(self, suit):
        super().__init__(13, suit)

    def __repr__(self):
        return PlayingCard.Names[self.suit] + 'King'


class AceCard(PlayingCard):
    """
    AceCard: class to represent an Ace
    """

    def __init__(self, suit, value=14):
        assert value == 1 or value == 14
        super().__init__(value, suit)

    def __repr__(self):
        return PlayingCard.Names[self.suit] + 'Ace'


class Deck(metaclass=ABCMeta):
    """
    Deck: Base class for a deck of cards

    Specific decks need to define how the deck is built up and implement the abstract method:
    _init(self)
    """

    def __init__(self, ordered=False):
        self.deck_size = 0
        self.no_cards = 0
        self.cards = []
        self._init(ordered)

    @abstractmethod
    def _init(self, ordered):
        pass

    def draw(self, number=1):
        assert number <= self.no_cards

        cards = [self.cards.pop()]
        for i in range(1, number):
            cards.append(self.cards.pop())

        self.no_cards -= number

        return cards

    def give_card(self):
        return self.draw()

    def shuffle(self):
        from random import shuffle

        shuffle(self.cards)

    def sort(self):
        self.cards.sort()


class StandardDeck(Deck):
    """
    StandardDeck: A standard deck with 52 cards
    """

    def _init(self, ordered):
        self.deck_size = 52
        for suit in Suit:
            for value in range(2, 11):
                self.cards.append(NumberedCard(value, suit))

            self.cards.append(JackCard(suit))
            self.cards.append(QueenCard(suit))
            self.cards.append(KingCard(suit))
            self.cards.append(AceCard(suit))

        self.no_cards = 52

        if not ordered:
            from random import shuffle

            self.shuffle()


class PokerHand(object):
    def __init__(self, hand_type, cards):
        self.hand_type = hand_type
        self.cards = cards

    def __lt__(self, other):
        return (self.hand_type, self.cards) < (other.hand_type, other.cards)

    def __repr__(self):
        return self.hand_type.name + ' ' + str(self.cards)


class Hand(object):
    """
    Hand: a class representing the hand of cards for a player
    """

    def __init__(self, max_size=5):
        self.cards = []
        self.max_size = max_size

    def add_card(self, cards):
        if not isinstance(cards, list):
            cards = [cards]
        assert len(self.cards) + len(cards) <= self.max_size

        self.cards.extend(cards)

    def _lay(self, cards, show=False):
        if cards is None:  # None -> lay all
            cards = list(range(self.count()))

        if isinstance(cards, int):
            cards = [cards]

        assert len(cards) <= len(self.cards)

        _cards = self.cards.copy()
        removed = []
        for card in cards:
            if isinstance(card, int):
                assert card < len(_cards)
                _card = _cards[card]
            else:
                _card = card

            assert _card in self.cards
            removed.append(_card)
            self.cards.remove(_card)

        if show:
            return removed
        else:
            return None

    def drop(self, cards=None):
        self._lay(cards)

    def play(self, cards=None):
        return self._lay(cards, show=True)

    def show(self):
        print(self.cards)
        pass

    def sort(self, reverse=False):
        self.cards.sort()
        if reverse:
            self.cards.reverse()

    def count(self):
        return len(self.cards)

    def _is_flush(self, required=5):
        counts = []
        for suit in range(4):
            counts.append(sum([x.suit == suit for x in self.cards]))

        if max(counts) >= required:
            return True

        return False

    def _is_straight(self, required=5):
        count = max_count = 0

        # Build list of unique values (using a set!), add Ace as 14 and 1!
        values = set()
        for card in self.cards:
            values.add(card.value)
            if card.value == 14:
                values.add(1)
            if card.value == 1:
                values.add(14)

        values = sorted(list(values))

        for i in range(1, len(values)):
            if values[i - 1] + 1 == values[i]:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0
            if count > max_count:
                max_count = count

        return max_count + 1 >= required

    def _get_counts(self):
        counts = dict()
        for card in self.cards:
            if card.value in counts.keys():
                counts[card.value] += 1
            else:
                counts[card.value] = 1

        # Create reverse-dict, i.e. count as key, values as items (in list)
        values = dict()
        for value, count in counts.items():
            if count in values:
                values[count] += [value]
            else:
                values[count] = [value]

        return values

    def best_combination(self, cards=list()):
        _full_hand = Hand(max_size=self.max_size + len(cards))
        _full_hand.add_card(self.cards)
        _full_hand.add_card(cards)
        _full_hand.sort()

        is_straight = _full_hand._is_straight()
        if _full_hand._is_flush():
            if is_straight:
                return PokerHand(HandType.StraightFlush, _full_hand.cards[-1])
            else:
                return PokerHand(HandType.Flush, _full_hand.cards[-1])

        if is_straight:
            return PokerHand(HandType.Straight, _full_hand.cards[-1])

        # Will return dictionary with count as key, and values for each count in list
        counts = _full_hand._get_counts()
        high_card = sorted(counts.items())[-1]  # Pick the highest count and its list of values
        high_card = sorted(high_card[1])[-1]  # Select the values, sort it and select highest value

        _full_hand.sort(reverse=True)
        for card in _full_hand.cards:  # Find highest Card
            if card.value == high_card:
                high_card = card
                break

        if max(counts.keys()) == 4:
            return PokerHand(HandType.FourOfAKind, high_card)

        if max(counts.keys()) == 3:
            if (2 in counts) or len(counts[3]) >= 2:
                return PokerHand(HandType.FullHouse, high_card)
            else:
                return PokerHand(HandType.ThreeOfAKind, high_card)

        if max(counts.keys()) == 2:
            if len(counts[2]) >= 2:
                return PokerHand(HandType.TwoPair, high_card)
            else:
                return PokerHand(HandType.OnePair, high_card)

        return PokerHand(HandType.HighCard, high_card)


class Player:
    """
    Player: A class representing the player
    """

    def __init__(self, name, wallet=0):
        self.name = name
        self.wallet = wallet
        self.hand = Hand()
        self.poker_hand = None

    def __str__(self):
        return 'Player: "{}", Wallet: {}, No. cards: {}'.format(self.name, self.wallet, self.hand.count())

    def add_money(self, amount):
        self.wallet += amount

    def bet(self, amount):
        if amount > self.wallet or amount <= 0:
            raise ValueError

        self.wallet -= amount
        return amount

    def add_cards(self, cards):
        self.hand.add_card(cards)

    def find_poker_hand(self, cards=[]):
        self.poker_hand = self.hand.best_combination(cards)


def five_card_draw(no_players, rounds):
    # Create (shuffled) deck
    deck = StandardDeck()

    # Create players
    players = list()
    for player in range(no_players):
        name = "Player " + str(player + 1)
        players.append(Player(name, 100))

    # Give first hand
    for player in players:
        player.add_cards(deck.draw(5))
        player.hand.sort()

    for round in range(rounds):
        print('\n Round :', round)

        for player in players:
            player.hand.sort()
            print(player, end='  ')
            player.hand.show()

            input_ok = False
            while not input_ok:
                text = input(" comma separated list index of cards to drop (starting from 1, empty for none): ")
                if not text:
                    input_ok = True
                    continue

                try:
                    drops = [int(a) for a in text.split(',')]
                except:
                    continue

                no_drops = len(drops)

                # Validate input
                input_ok = True
                for i in drops:
                    if not 1 <= i <= 5:
                        input_ok = False
                        break

                drops = np.array(drops) - 1
                player.hand.drop(drops.tolist())
                player.add_cards(deck.draw(no_drops))

    print('\nResults:')
    for player in players:
        player.hand.sort()
        print(player, end='  ')
        player.hand.show()
        player.find_poker_hand()
        print(' Hand:', player.poker_hand)

    print('\nSorted results:')
    for player in sorted(players, key=lambda x: x.poker_hand):
        print(player, end='  ')
        player.hand.show()
        print(' Hand:', player.hand.best_combination())


def texas_holdem(no_players):
    # Create (shuffled) deck
    deck = StandardDeck()

    # Create players
    players = list()
    for player in range(no_players):
        name = "Player " + str(player + 1)
        players.append(Player(name, 100))

    # Give first hand
    for player in players:
        player.add_cards(deck.draw(2))
        player.hand.sort()
        print(player, end='  ')
        player.hand.show()

    table = Hand()
    table.add_card(deck.draw(3))
    print('Table:', end='  ')
    table.show()
    print()

    for player in players:
        print(player, end='  ')
        player.find_poker_hand(table.cards)
        print(player.poker_hand)

    # BET

    for round in range(2):
        table.add_card(deck.draw())
        print('\nTable:', end='  ')
        table.show()

        for player in players:
            print(player, end='  ')
            player.find_poker_hand(table.cards)
            print(player.poker_hand)

        print()
        # BET

    # SHOW
    print('Table:', end='  ')
    table.sort()
    table.show()
    print('\nSorted results:')
    for player in sorted(players, key=lambda x: x.poker_hand):
        print(player, end='  ')
        player.hand.show()
        print(' PokerHand:', player.poker_hand)


if __name__ == "__main__":

    game_type = 0
    while not 0 < game_type < 3:
        text = input("Choose game type: 1 for 5 card draw, 2 for Texas Hold'em: ")
        try:
            game_type = int(text)
        except:
            print('"%s" is not an integer!' % text)

    no_players = None
    # no_players = 2
    rounds = 2

    while not isinstance(no_players, int):
        text = input("Enter no. of players: ")
        try:
            no_players = int(text)
        except:
            print('"%s" is ot an integer!' % text)

    print("No players:", no_players)

    if game_type == 1:
        five_card_draw(no_players, rounds)
    else:
        texas_holdem(no_players)
