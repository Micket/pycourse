from collections import Counter # Counter is convenient for counting objects (a specialized dictionary)

def check_straight_flush(cards):
    """
    Checks for the best straight flush in a list of cards (may be more than just 5)

    :param cards: A list of playing cards.
    :return: None if no straight flush is found, else the value of the top card.
    """
    vals = [(c.give_value(), c.suit) for c in cards] \
        + [(1, c.suit) for c in cards if c.give_value() == 14]  # Add the aces!
    for c in reversed(cards): # Starting point (high card)
        # Check if we have the value - k in the set of cards:
        found_straight = True
        for k in range(1, 5):
            if (c.give_value() - k, c.suit) not in vals:
                found_straight = False
                break
        if found_straight:
            return c.give_value()


def check_full_house(cards):
    """
    Checks for the best full house in a list of cards (may be more than just 5)

    :param cards: A list of playing cards
    :return: None if no full house is found, else a tuple of the values of the triple and pair.
    """
    value_count = Counter()
    for c in cards:
        value_count[c.give_value()] += 1
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
                return three, two
