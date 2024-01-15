from collections import Counter # Counter is convenient for counting objects (a specialized dictionary)

def check_straight_flush(cards):
    """
    Checks for the best straight flush in a list of cards (may be more than just 5)

    :param cards: A list of playing cards sorted by value.
    :return: None if no straight flush is found, else the value of the top card.
    """
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


def check_full_house(cards):
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
    threes.sort(reverse=True)
    # Find the card ranks that have at least a pair
    twos = [v[0] for v in value_count.items() if v[1] >= 2]
    twos.sort(reverse=True)

    # Threes are dominant in full house, lets check that value first:
    for three in threes:
        for two in twos:
            if two != three:
                return three, two


def check_flush(cards):
    """
    Checks for the best full house in a list of cards (may be more than just 5)

    :param cards: A list of playing cards
    :return: None if no flush is found, else highest 5 values of flush
    """

    # Needlessly general for conventional poker games:
    # this makes no assumptions on the total number of cards
    # Group cards by suit:
    by_suit = defaultdict(list)
    for c in cards:
        by_suit[c.suit].append(c.get_value())

    # Look for best suit-grouped cards
    best_values = [0]
    for values in by_suit.values():
        if len(cards) >= 5 and max(values) > max(best_values):
            best_values = values
    if max(best_values) > 0:
        return best_values[:5]
