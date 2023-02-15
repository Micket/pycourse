import abc
from PyQt5.QtCore import QObject, pyqtSignal  # no GUI stuff inside this file!

# NOTE: This is just given as an example of how to use CardsView.
# It is expected that you will need to adjust things to make a game out of it. 

class QABCMeta(abc.ABCMeta, type(QObject)):
    # This metaclass wrapper is necessary when dealing with multiple inherited metaclasses:
    # We want ABCMeta and the metaclass for QOBject (which does the signal handling)
    # https://stackoverflow.com/questions/28799089/python-abc-multiple-inheritance
    # You don't need to understand the subtleties of this in this course.
    # The exam won't cover multiple inheritance of metaclasses.
    pass


class CardsModel(QObject, metaclass=QABCMeta):
    """ Base class that described what is expected from the CardsView widget. """

    new_cards = pyqtSignal()  #: Signal should be emited when cards change.

    @abc.abstractmethod
    def __iter__(self):
        """Returns an iterator of card objects"""

    @abc.abstractmethod
    def flipped(self):
        """Returns true of cards should be drawn face down"""

    @abc.abstractmethod
    def flip(self):
        """Returns true of cards should be drawn face down"""


# A trivial card class (you should use the stuff you made in your library instead!)
class MySimpleCard:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value


# You have made a class similar to this (hopefully):
class Hand:
    def __init__(self):
        # Lets use some hardcoded values for most of this to start with
        self.cards = [MySimpleCard(13, 2), MySimpleCard(7, 0), MySimpleCard(13, 1)]

    def add_card(self, card):
        self.cards.append(card)


# We can extend this class to create a model, which updates the view whenever it has changed.
# NOTE: You do NOT have to do it this way.
# You might find it easier to make a Player-model, or a whole GameState-model instead.
# This is just to make a small demo that you can use. You are free to modify
class HandModel(Hand, CardsModel):
    def __init__(self):
        Hand.__init__(self)
        CardsModel.__init__(self)
        # Additional state needed by the UI
        self.flipped_cards = False

    def __iter__(self):
        return iter(self.cards)

    def flip(self):
        # Flips over the cards (to hide them)
        self.flipped_cards = not self.flipped_cards
        self.new_cards.emit()  # something changed, better emit the signal!

    def flipped(self):
        # This model only flips all or no cards, so we don't care about the index.
        # Might be different for other games though!
        return self.flipped_cards

    def add_card(self, card):
        # This method mutates the object, so we must of course 
        super().add_card(card)
        self.new_cards.emit()  # something changed, better emit the signal!

