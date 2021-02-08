import pytest
from enum import Enum
from cardlib import *


# This test assumes you call your suit class "Suit" and the colours "Hearts and "Spades"
def test_cards():
    h5 = NumberedCard(4, Suit.Hearts)
    assert isinstance(h5.suit, Enum)

    sk = KingCard(Suit.Spades)
    assert sk.get_value() == 13

    assert h5 < sk
    assert h5 == h5


# This test assumes you call your shuffle method "shuffle" and the method to draw a card "draw"
def test_deck():
    d = StandardDeck()
    c1 = d.draw()
    c2 = d.draw()
    assert not c1 == c2

    d2 = StandardDeck()
    d2.shuffle()
    c3 = d2.draw()
    c4 = d2.draw()
    assert not ((c3, c4) == (c1, c2))


# This test builds on the assumptions above and assumes you store the cards in the hand in the list "cards",
# and that your sorting method is called "sort" and sorts in increasing order
def test_hand():
    h = Hand()
    assert len(h.cards) == 0
    d = StandardDeck()
    d.shuffle()
    h.add_card(d.draw())
    h.add_card(d.draw())
    h.add_card(d.draw())
    h.add_card(d.draw())
    h.add_card(d.draw())
    assert len(h.cards) == 5

    h.sort()
    for i in range(3):
        assert h.cards[i] < h.cards[i+1] or h.cards[i] == h.cards[i+1]

    cards = h.cards.copy()
    h.drop_cards([3, 0, 1])
    assert len(h.cards) == 2
    assert h.cards[0] == cards[2]
    assert h.cards[1] == cards[4]


def test_pokerhands():
    h1 = Hand()
    h1.add_card(QueenCard(Suit.Diamonds))
    h1.add_card(KingCard(Suit.Hearts))

    h2 = Hand()
    h2.add_card(QueenCard(Suit.Hearts))
    h2.add_card(AceCard(Suit.Hearts))

    cl = [NumberedCard(10, Suit.Diamonds), NumberedCard(9, Suit.Diamonds),
          NumberedCard(8, Suit.Clubs), NumberedCard(6, Suit.Spades)]

    ph1 = h1.best_poker_hand(cl)
    assert isinstance(ph1, PokerHand)
    ph2 = h2.best_poker_hand(cl)
    # assert ph1 == PokerHand( <insert your handtype class and data here> )
    # assert ph2 == PokerHand( <insert your handtype class and data here> )

    assert ph1 < ph2

    cl.pop(0)
    cl.append(QueenCard(Suit.Spades))
    ph3 = h1.best_poker_hand(cl)
    ph4 = h2.best_poker_hand(cl)
    assert ph3 < ph4
    assert ph1 < ph2

    # assert ph3 == PokerHand( <insert your handtype class and data here> )
    # assert ph4 == PokerHand( <insert your handtype class and data here> )

    cl = [QueenCard(Suit.Clubs), QueenCard(Suit.Spades), KingCard(Suit.Clubs), KingCard(Suit.Spades)]
    ph5 = h1.best_poker_hand(cl)
    # assert ph5 == PokerHand( <insert your handtype for a Full House and data here> )
