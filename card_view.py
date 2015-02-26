from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSvg import *
import sys


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

    # Underscores indicate a private function!
    def __read_cards(): # Ignore the PyCharm warning on this line. It's correct.
        """
        Reads all the 52 cards from files.
        :return: Dictionary of SVG renderers
        """
        all_cards = dict()
        for suit in 'HDSC':
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                file = value + suit
                # Since everyone did their PlayingCard differently, I'm just using a string for now.
                all_cards[file] = QSvgRenderer('cards/' + file + '.svg')
        return all_cards

    # We read all the card graphics as static class variables
    back_card = QSvgRenderer('cards/Red_Back_2.svg')
    all_cards = __read_cards()

    def __init__(self, game_state, player, card_spacing=250, padding=10):

        self.scene = TableScene()
        super().__init__(self.scene)

        self.player = player
        self.card_spacing = card_spacing
        self.padding = padding
        player.set_callback(self.change_cards)

        self.change_cards()  # Add the cards the first time around to represent the initial state.

    def change_cards(self):
        # Add the cards from scratch
        self.scene.clear()
        for i, c_ref in enumerate(self.player.cards):
            renderer = self.back_card if self.player.marked_cards[i] else self.all_cards[c_ref]
            c = CardSvgItem(renderer, i)
            self.scene.addItem(c)

        self.update_view()

    def update_view(self):
        for c in self.scene.items():
            # Lets have the cards take up almost the (current) full height
            card_height = c.boundingRect().bottom()
            scale = (self.height()-2*self.padding)/card_height

            c.setPos(c.position * self.card_spacing*scale, 0)
            c.setScale(scale)
            #c.setOpacity(0.5 if self.player.marked_cards[c.position] else 1.0)

        # Put the scene bounding box
        self.scene.setSceneRect(-self.padding, -self.padding, self.viewport().width(), self.viewport().height())


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
            self.player.mark_position(item.position)


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


class Player:
    def __init__(self):
        # Lets use some hardcoded values for most of this to start with
        self.cards = ['QS', 'AD', '7C']
        self.marked_cards = [False]*len(self.cards)
        self.flipped = False
        self.credits = 100
        self.folded = False
        self.cb = None

    def set_callback(self, cb):
        # Instead of the sophisticated signal system, I have a simple callback here.
        # This only works if there is just one viewer!
        # But I want to reduce the complexity in this example to make it clear why things occur.
        self.cb = cb

    def active(self):
        return credits > 0 and not self.folded

    def mark_position(self, i):
        # Mark the card as position "i" to be thrown away
        self.marked_cards[i] = not self.marked_cards[i]
        if self.cb is not None: self.cb()


# Lets test it out
app = QApplication(sys.argv)
p = Player()
game_state = GameState([p])

card_view = CardView(game_state, p)
box = QVBoxLayout()
box.addWidget(card_view)
player_view = QGroupBox("Player 1")
player_view.setLayout(box)
player_view.show()

app.exec_()