from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSvg import *
import sys
#import card_game as cg

class TableScene(QGraphicsScene):
    """ A scene with a table cloth background """
    def __init__(self):
        super().__init__()
        self.tile = QPixmap('cards/table.png')
        self.setBackgroundBrush(self.tile)


class CardSvgItem(QGraphicsSvgItem):
    """ A simple overloaded QGraphicsSvgItem that also stores the card position """
    def __init__(self, renderer, id):
        super().__init__()
        self.setSharedRenderer(renderer)
        self.position = id


class CardView(QGraphicsView):
    """ A View widget that represents the
    """

    # Underscores indicate a private function/method!
    def __read_cards(): # Ignore the PyCharm warning on this line. It's correct.
        """
        Reads all the 52 cards from files.
        :return: Dictionary of SVG renderers
        """
        all_cards = dict() # Dictionaries let us have convenient mappings between cards and their images
        for suit_file, suit in zip('HDSC', range(4)): # Check the order of the suits here!!!
            for value_file, value in zip(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], range(2, 15)):
                file = value_file + suit_file
                key = (value, suit)  # I'm choosing this tuple to be the key for this dictionary
                all_cards[key] = QSvgRenderer('cards/' + file + '.svg')
        return all_cards

    # We read all the card graphics as static class variables
    back_card = QSvgRenderer('cards/Red_Back_2.svg')
    all_cards = __read_cards()

    def __init__(self, cards_model, card_spacing=250, padding=10):
        """
        Initializes the view to display the content of the given model
        :param cards_model: A model that represents a set of cards.
        The model should have: data_changed, cards, clicked_position, flipped,
        :param card_spacing: Spacing between the visualized cards.
        :param padding: Padding of table area around the visualized cards.
        """
        self.scene = TableScene()
        super().__init__(self.scene)

        self.model = cards_model
        self.card_spacing = card_spacing
        self.padding = padding

        # The view should listen to changes:
        cards_model.data_changed.connect(self.change_cards)
        # Add the cards the first time around to represent the initial state.
        self.change_cards()

    def change_cards(self):
        # Add the cards from scratch
        self.scene.clear()
        for i, card in enumerate(self.model.cards):
            # The ID of the card in the dictionary of images is a tuple with (value, suit), both integers
            # TODO: YOU MUST CORRECT THE EXPRESSION TO MATCH YOUR PLAYING CARDS!!!
            # TODO: See the __read_cards method for what mapping are used.
            graphics_key = (card.value, card.suit)
            renderer = self.back_card if self.model.flipped(i) else self.all_cards[graphics_key]
            c = CardSvgItem(renderer, i)
            # Sets the opacity of cards if they are marked.
            c.setOpacity(0.5 if self.model.marked(c.position) else 1.0)
            self.scene.addItem(c)

        self.update_view()

    def update_view(self):
        for c in self.scene.items():
            # Lets have the cards take up almost the (current) full height
            card_height = c.boundingRect().bottom()
            scale = (self.height()-2*self.padding)/card_height

            c.setPos(c.position * self.card_spacing*scale, 0)
            c.setScale(scale)

        # Put the scene bounding box
        self.setSceneRect(-self.padding, -self.padding, self.viewport().width(), self.viewport().height())


    def resizeEvent(self, painter):
        # This method is called when the window is resized.
        # If the widget is resize, we gotta adjust the card sizes.
        # QGraphicsView automatically re-paints everything when we modify the scene.
        self.update_view()
        super().resizeEvent(painter)

    # This is the Controller part of the GUI, handling input events that modify the Model
    def mousePressEvent(self, event):
        # We can check which item, if any, that we clicked on by fetching the scene items (neat!)
        item = self.scene.itemAt(event.pos())
        if item is not None:
            # Report back that the user clicked on the card at given position:
            # The model can choose to do whatever it wants with this information.
            self.model.clicked_position(item.position)


    # You can remove these events if you don't need them.
    def mouseDoubleClickEvent(self, event):
        self.model.flip() # Another possible event. Lets add it to the flip functionality for fun!


class GameState:
    def __init__(self, players):
        self.players = players
        self.starting_player = -1
        self.player_turn = 0
        self.player_raise = 0
        self.table_cards = []
        self.pot = 0
        self.last_bet = 0
        #self.deck = pc.Deck()

    def start_round(self):
        self.deck = pc.Deck()
        self.deck.shuffle()
        self.table_cards = []

        self.starting_player += 1
        self.player_turn = self.starting_player
        self.player_raise = self.starting_player

        for p in self.players:
            p.hand.clear()
            p.folded = False
            for i in range(2):
                p.hand.add_card(self.deck.pop())

    def player_fold(self, player):
        self.players[player].folded = True

    def player_bet(self, player, amount):
        if player != self.player_turn:
            # Should not try to bet when it's not your turn!
            return

        if amount != self.last_bet:
            self.last_bet = amount
            self.player_raise = self.player_turn

        self.pot += amount

        # Go to next active player
        self.player_turn += 1
        while self.players[self.player_turn].active():
            self.player_turn += 1

    def distribute_pot(self, winners):
        # TODO
        for p in self.players:
            p.add_credits(self.pot / len(self.players))


# Example code below for how to connect to your game state:

# A trivial card class (you should use the stuff you made in your library instead!
class MySimpleCard:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

# You have made a class like this (hopefully). I'm just using a simple version here:
class Hand:
    def __init__(self):
        # Lets use some hardcoded values for most of this to start with
        self.cards = [MySimpleCard(13, 2), MySimpleCard(7, 0), MySimpleCard(13, 1)]

    def add_card(self, card):
        self.cards.append(card)


class HandModel(Hand, QObject):
    data_changed = Signal()

    def __init__(self):
        Hand.__init__(self)
        QObject.__init__(self)

        # Additional state needed by the UI, keeping track of the selected cards:
        self.marked_cards = [False]*len(self.cards)
        self.flipped_cards = True

    def flip(self):
        # Flips over the cards (to hide them)
        self.flipped_cards = not self.flipped_cards
        self.data_changed.emit()

    def marked(self, i):
        return self.marked_cards[i]

    def flipped(self, i):
        # This model only flips all or no cards, so we don't care about the index.
        # Might be different for other games though!
        return self.flipped_cards

    def clicked_position(self, i):
        # Mark the card as position "i" to be thrown away
        self.marked_cards[i] = not self.marked_cards[i]
        self.data_changed.emit()

    def add_card(self, card):
        super().add_card(card)
        self.data_changed.emit()



# Lets test it out
app = QApplication(sys.argv)
hand = HandModel()

card_view = CardView(hand)

# Creating a small demo window to work with, and put the card_view inside:
box = QVBoxLayout()
box.addWidget(card_view)
player_view = QGroupBox("Player 1")
player_view.setLayout(box)
player_view.show()

app.exec_()