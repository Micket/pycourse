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
    def __init__(self, path, id):
        super().__init__(path)
        self.id = id


class CardView(QGraphicsView):
    def __init__(self, game_state, player, card_spacing=250, padding=10):

        self.scene = TableScene()
        super().__init__(self.scene)

        self.game_state = game_state
        self.player = player
        self.card_spacing = card_spacing
        self.padding = padding

        # Cache all the SVG items:
        self.all_cards = dict()
        self.back_cards = dict()
        for suit in 'HDSC':
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                id = value + suit
                self.all_cards[id] = CardSvgItem('cards/' + id + '.svg', id)
                self.back_cards[id] = CardSvgItem('cards/Red_Back_2.svg', id)
        # I don't really like the SVG api here. I can only create SvgItems, not Svg graphics.
        # Therefor, I need duplicates. since the items themselves store the positions.

    def paintEvent(self, painter):
        # This method is called whenever the view needs to be repainted (e.g. re-sized window).

        # Remove items without deleting! (scene.clear() deletes the graphics)
        for item in self.scene.items():
            self.scene.removeItem(item)

        card_height = self.back_cards['2H'].boundingRect().bottom()

        # Lets have the cards take up almost the (current) full height
        scale = (self.height()-3*self.padding)/card_height

        # Add the cards:
        for i, c_ref in enumerate(self.player.cards):
            if self.player.flipped:
                c = self.back_cards[c_ref]
            else:
                c = self.all_cards[c_ref]
            self.scene.addItem(c)
            c.setPos(i * self.card_spacing*scale, 0)
            c.setScale(scale)
            c.setOpacity(0.5 if self.player.marked(c_ref) else 1.0)

        # Put the scene bounding box slightly
        self.scene.setSceneRect(-self.padding, -self.padding, self.width() - 5, self.height() - 5)

        # Call the paint event for QGraphicsView
        super().paintEvent(painter)

    def mousePressEvent(self, event):
        item = self.scene.itemAt(event.pos())
        if item is not None:
            self.player.mark_position(item.id)


class GameState:
    def __init__(self, players):
        self.players = players
        self.starting_player = -1;
        self.table_cards = []
        self.pot = 0.

    def start_round(self):
        self.deck = pc.Deck()
        self.deck.shuffle()
        self.table_cards = []

        self.starting_player += 1
        self.player_turn = self.player_start
        self.last_raise = player

        for p in self.players:
            p.hand.clear()
            for i in range(2):
                p.hand.add_card(self.deck.pop())

    def player_fold(self, player, amount):
        pass

    def player_bet(self, player, amount):
        if player != self.player_turn:
            # Should not try to bet when it's not your turn!
            return

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
        self.cards = []
        self.marked_cards = dict() #{c : False for c in self.cards}
        self.flipped = False
        self.credits = 100

    def active(self):
        return credits > 0 and len(self.cards) > 0

    def mark_position(self, id):
        pass
        #self.marked_cards[id] = not self.marked_cards[id]

    def marked(self, id):
        return False
        #return self.marked_cards[id]

app = QApplication(sys.argv)
game_state = GameState()
player = Player()
view = CardView(game_state, player)
view.show()
app.exec_()