import pytest
from collections import Counter
from cardlib import *

HAND_HAS_STR = True
MY_HAND_FORMAT = False


def print_hand(h):
    if HAND_HAS_STR:
        print(h)
    else:
        for c in h.cards:
            print(c, end=', ')
        print()


cards = []
for suit in Suit:
    for number in range(2, 11):
        cards.append(NumberedCard(number, suit))
    cards.append(JackCard(suit))
    cards.append(QueenCard(suit))
    cards.append(KingCard(suit))
    cards.append(AceCard(suit))


def test_suit():
    suits = [suit for suit in Suit]
    assert suits[0] == Suit.Hearts
    assert suits[1] == Suit.Spades
    assert suits[2] == Suit.Clubs
    assert suits[3] == Suit.Diamonds


def test_basic_cards():
    assert len(cards) == 52
    for i in range(12):
        assert cards[i] < cards[i + 1]

    with pytest.raises(TypeError):
        pc = PlayingCard(Suit.Clubs)


def test_card_types():
    assert cards[0] == NumberedCard(2, Suit.Hearts)
    assert type(str(cards[14])) == str


def test_deck_basics():
    d = StandardDeck()
    values = list()
    suits = list()
    for i in range(52):
        c = d.draw()
        values.append(c.get_value())
        suits.append(c.suit)
        assert isinstance(c, PlayingCard)

    vc = Counter(values)
    for i in range(2, 15):
        assert vc[i] == 4
    sc = Counter(suits)
    for s in Suit:
        assert sc[s] == 13

    with pytest.raises(Exception):
        d.draw()


def test_deck_shuffle():
    d = StandardDeck()
    cards1 = list()
    for i in range(5):
        cards1.append(d.draw())
    d = StandardDeck()
    none = d.shuffle()
    assert none == None
    cards2 = list()
    for i in range(5):
        cards2.append(d.draw())
    assert cards1 != cards2


def test_hand_drop():
    h = Hand()
    h2 = Hand()
    d = StandardDeck()
    d.shuffle()
    for i in range(5):
        c = d.draw()
        h.add_card(c)
        h2.add_card(c)
    print()
    print_hand(h)
    h.drop_cards([3, 0, 4])
    print_hand(h)
    assert h.cards[0] == h2.cards[1]
    assert h.cards[1] == h2.cards[2]


def test_hand_sort():
    h = Hand()
    d = StandardDeck()
    d.shuffle()
    for i in range(5):
        c = d.draw()
        h.add_card(c)
    h.sort()
    for i in range(len(h.cards) - 1):
        assert (not h.cards[i] > h.cards[i + 1]) or (not h.cards[i] < h.cards[i + 1])


def test_hand_str():
    h = Hand()
    assert type(str(h)) == str


def test_hand_best_pokerhand():
    h = Hand()
    d = StandardDeck()
    d.shuffle()
    for i in range(5):
        c = d.draw()
        h.add_card(c)
    hcards = h.cards.copy()
    print()
    print_hand(h)
    ph = h.best_poker_hand()
    assert type(ph) == PokerHand
    assert hcards == h.cards
    print(ph)
    cards = list()
    cards.extend([d.draw(), d.draw()])
    print("[" + ", ".join(str(c) for c in cards) + "]")
    ph2 = h.best_poker_hand(cards)
    assert hcards == h.cards
    print_hand(h)
    print(ph2)
    print(ph < ph2)


def _get_basic_hands_and_cards():
    h1 = Hand()
    h1.add_card(QueenCard(Suit.Hearts))
    h1.add_card(KingCard(Suit.Hearts))

    h2 = Hand()
    h2.add_card(QueenCard(Suit.Hearts))
    h2.add_card(AceCard(Suit.Hearts))

    cl = [NumberedCard(10, Suit.Diamonds), NumberedCard(9, Suit.Diamonds), NumberedCard(8, Suit.Clubs),
          NumberedCard(6, Suit.Spades)]

    return h1, h2, cl


def test_ph_highcard():
    h1, h2, cl = _get_basic_hands_and_cards()
    ph1 = h1.best_poker_hand(cl)
    ph2 = h2.best_poker_hand(cl)
    if MY_HAND_FORMAT:
        assert ph1 == PokerHand(HandType.HighCard, [13, 12, 10, 9, 8])
        assert ph2 == PokerHand(HandType.HighCard, [14, 12, 10, 9, 8])
    print()
    print(f"ph1: {ph1}")
    print(f"ph2: {ph2}")
    assert ph1 < ph2


def test_ph_pair():
    h1, h2, cl = _get_basic_hands_and_cards()
    cl.pop(0)
    cl.append(QueenCard(Suit.Spades))
    ph2 = h1.best_poker_hand(cl)
    ph3 = h2.best_poker_hand(cl)
    if MY_HAND_FORMAT:
        assert ph2 == PokerHand(HandType.OnePair, [12, 13, 9, 8])
        assert ph3 == PokerHand(HandType.OnePair, [12, 14, 9, 8])
    print()
    print(f"ph2: {ph2}")
    print(f"ph3: {ph3}")
    assert ph2 < ph3


def test_ph_twopair():
    h1, h2, cl = _get_basic_hands_and_cards()
    cl.pop(0)
    cl.append(QueenCard(Suit.Spades))
    cl.append(NumberedCard(9, Suit.Clubs))
    ph3 = h1.best_poker_hand(cl)
    ph4 = h2.best_poker_hand(cl)
    if MY_HAND_FORMAT:
        assert ph3 == PokerHand(HandType.TwoPair, [12, 9, 13])
        assert ph4 == PokerHand(HandType.TwoPair, [12, 9, 14])
    print()
    print(f"ph3: {ph3}")
    print(f"ph4: {ph4}")
    assert ph3 < ph4


def test_ph_threeofakind():
    h1, h2, cl = _get_basic_hands_and_cards()
    cl.pop(0)
    cl.append(QueenCard(Suit.Spades))
    cl.append(QueenCard(Suit.Diamonds))
    ph4 = h1.best_poker_hand(cl)
    ph5 = h2.best_poker_hand(cl)
    if MY_HAND_FORMAT:
        assert ph4 == PokerHand(HandType.ThreeOfAKind, [12, 13, 9])
        assert ph5 == PokerHand(HandType.ThreeOfAKind, [12, 14, 9])
    print()
    print(f"ph4: {ph4}")
    print(f"ph5: {ph5}")
    assert ph4 < ph5


def test_ph_fullhouse():
    h1, h2, cl = _get_basic_hands_and_cards()
    cl.pop(0)
    cl.append(QueenCard(Suit.Spades))
    cl.append(QueenCard(Suit.Diamonds))
    cl.append(NumberedCard(9, Suit.Clubs))
    ph5 = h1.best_poker_hand(cl)
    ph6 = h2.best_poker_hand(cl)
    if MY_HAND_FORMAT:
        assert ph5 == PokerHand(HandType.FullHouse, [12, 9])
        assert ph6 == PokerHand(HandType.FullHouse, [12, 9])
    print()
    print(f"ph5: {ph5}")
    print(f"ph6: {ph6}")
    assert ph5 == ph6


def test_ph_fourofakind():
    h1, h2, cl = _get_basic_hands_and_cards()
    cl.pop(0)
    cl.append(QueenCard(Suit.Spades))
    cl.append(QueenCard(Suit.Diamonds))
    cl.append(QueenCard(Suit.Clubs))
    ph6 = h1.best_poker_hand(cl)
    cl.append(AceCard(Suit.Spades))
    ph7 = h1.best_poker_hand(cl)
    if MY_HAND_FORMAT:
        assert ph6 == PokerHand(HandType.FourOfAKind, [12, 13])
        assert ph7 == PokerHand(HandType.FourOfAKind, [12, 14])
    print()
    print(f"ph6: {ph6}")
    print(f"ph7: {ph7}")
    assert ph6 < ph7


def test_ph_straight():
    h1, h2, _ = _get_basic_hands_and_cards()
    cl = [JackCard(Suit.Hearts), NumberedCard(10, Suit.Hearts), NumberedCard(5, Suit.Spades), QueenCard(Suit.Clubs),
          NumberedCard(9, Suit.Diamonds)]
    ph7 = h1.best_poker_hand(cl)
    cl.pop()
    cl.append(AceCard(Suit.Spades))
    ph8 = h1.best_poker_hand(cl)
    if MY_HAND_FORMAT:
        assert ph7 == PokerHand(HandType.Straight, [13])
        assert ph8 == PokerHand(HandType.Straight, [14])
    assert ph7 < ph8


def test_ph_straightflush():
    h1, h2, _ = _get_basic_hands_and_cards()
    cl = [JackCard(Suit.Hearts), NumberedCard(10, Suit.Hearts), NumberedCard(5, Suit.Spades), QueenCard(Suit.Clubs),
          AceCard(Suit.Hearts)]
    ph8 = h1.best_poker_hand(cl)
    if MY_HAND_FORMAT:
        assert ph8 == PokerHand(HandType.StraightFlush, [14])
    print()
    print(f"ph8: {ph8}")


def test_ph_flush():
    h1, h2, _ = _get_basic_hands_and_cards()
    cl = [JackCard(Suit.Hearts), NumberedCard(10, Suit.Hearts), NumberedCard(5, Suit.Spades),
          NumberedCard(5, Suit.Hearts)]
    ph9 = h1.best_poker_hand(cl)
    if MY_HAND_FORMAT:
        assert ph9 == PokerHand(HandType.Flush, [13, 12, 11, 10, 5])
    print()
    print(f"ph9: {ph9}")


def test_ph_ranks():
    h1, h2, cl = _get_basic_hands_and_cards()
    ph1 = h1.best_poker_hand(cl)  # High card

    cl.pop(0)
    cl.append(QueenCard(Suit.Spades))
    ph2 = h1.best_poker_hand(cl)  # One pair
    print()
    print(f"ph1: {ph1}")
    print(f"ph2: {ph2}")
    assert ph1 < ph2

    c1 = NumberedCard(9, Suit.Clubs)
    cl.append(c1)
    ph3 = h1.best_poker_hand(cl)  # Two pair
    print(f"\nph3: {ph3}")
    assert ph2 < ph3

    cl.pop()
    cl.append(QueenCard(Suit.Diamonds))
    ph4 = h1.best_poker_hand(cl)  # Three of a kind
    print(f"\nph4: {ph4}")
    assert ph3 < ph4

    cl.append(c1)
    ph5 = h1.best_poker_hand(cl)  # Full house
    print(f"\nph5: {ph5}")
    assert ph4 < ph5

    cl.append(QueenCard(Suit.Clubs))
    ph6 = h1.best_poker_hand(cl)  # Four of a kind
    print(f"\nph6: {ph6}")
    assert ph5 < ph6

    cl = [JackCard(Suit.Hearts), NumberedCard(10, Suit.Hearts), NumberedCard(5, Suit.Spades), QueenCard(Suit.Clubs),
          NumberedCard(9, Suit.Diamonds)]
    ph7 = h1.best_poker_hand(cl)  # Straight
    print(f"\nph7: {ph7}")
    assert ph4 < ph7

    cl.pop()
    cl.append(AceCard(Suit.Hearts))
    ph8 = h1.best_poker_hand(cl)  # Straight flush
    print(f"\nph8: {ph8}")
    assert ph6 < ph8

    cl.pop()
    cl.pop()
    cl.append(NumberedCard(5, Suit.Hearts))
    ph9 = h1.best_poker_hand(cl)  # Flush
    print(f"\nph9: {ph9}")
    assert ph9 < ph5
    assert ph7 < ph9
