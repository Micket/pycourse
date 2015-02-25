from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSvg import *
import sys


class TableScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.tile = QPixmap('cards/table.png')
        self.setBackgroundBrush(self.tile)


class CardSvgItem(QGraphicsSvgItem):
    def __init__(self, renderer, id):
        super().__init__()
        self.setSharedRenderer(renderer)
        self.position = id


class CardView(QGraphicsView):
    def __init__(self, game_state, player, card_spacing=250, padding=10):

        self.scene = TableScene()
        super().__init__(self.scene)

        self.game_state = game_state
        self.player = player
        self.card_spacing = card_spacing
        self.padding = padding

        # Cache all the SVG renderers:
        self.all_cards = dict()
        self.back_cards = dict()
        for suit in 'HDSC':
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                id = value + suit
                self.all_cards[id] = QSvgRenderer('cards/' + id + '.svg')
        self.back_card = QSvgRenderer('cards/Red_Back_2.svg')

    def paintEvent(self, painter):
        # This method is called whenever the view needs to be repainted (e.g. re-sized window).

        # Add the cards from scratch:
        self.scene.clear()
        for i, c_ref in enumerate(self.player.cards):
            renderer = self.back_card if self.player.flipped else self.all_cards[c_ref]

            c = CardSvgItem(renderer, i)

            # Lets have the cards take up almost the (current) full height
            card_height = c.boundingRect().bottom()
            scale = (self.height()-3*self.padding)/card_height

            c.setPos(i * self.card_spacing*scale, 0)
            c.setScale(scale)
            c.setOpacity(0.5 if self.player.marked_cards[i] else 1.0)
            self.scene.addItem(c)

        # Put the scene bounding box (the -5 is because the width include the window borders)
        self.scene.setSceneRect(-self.padding, -self.padding, self.width() - 5, self.height() - 5)

        # Call the paint event for QGraphicsView
        super().paintEvent(painter)

    def mousePressEvent(self, event):
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
        self.cards = ['QS', 'AD', '7C']
        self.marked_cards = [False]*len(self.cards)
        self.flipped = False
        self.credits = 100
        self.folded = False

    def active(self):
        return credits > 0 and not self.folded

    def mark_position(self, id):
        self.marked_cards[id] = not self.marked_cards[id]

    def marked(self, id):
        return self.marked_cards[id]

app = QApplication(sys.argv)
p = Player()
game_state = GameState([p])
view = CardView(game_state, p)
view.show()
app.exec_()