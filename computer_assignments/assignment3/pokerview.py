from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtSvg import *
from PyQt5.QtWidgets import *

import cardlib as cl
import pokermodel as pm


class TableScene(QGraphicsScene):
    """ A scene with a table cloth background """
    def __init__(self):
        super().__init__()
        self.tile = QPixmap('cards/table.png')
        self.setBackgroundBrush(QBrush(self.tile))


class CardItem(QGraphicsSvgItem):
    """ A simple overloaded QGraphicsSvgItem that also stores the card position """
    def __init__(self, renderer, position):
        super().__init__()
        self.setSharedRenderer(renderer)
        self.position = position


def read_cards():
    """
    Reads all the 52 cards from files.
    :return: Dictionary of SVG renderers
    """
    all_cards = dict()  # Dictionaries let us have convenient mappings between cards and their images
    for suit in cl.Suit:
        for value_file, value in zip(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], range(2, 15)):
            file = value_file + suit.name[0].upper()
            key = (value, suit)  # I'm choosing this tuple to be the key for this dictionary
            all_cards[key] = QSvgRenderer('cards/' + file + '.svg')
    return all_cards


class CardView(QGraphicsView):
    """ A View widget that represents the table area displaying a players cards. """

    # We read all the card graphics as static class variables
    back_card = QSvgRenderer('cards/Red_Back_2.svg')
    all_cards = read_cards()

    def __init__(self, cards_model: pm.CardModel, card_spacing=250, padding=10):
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

        # Whenever the this window should update, it should call the "change_cards" method.
        # This can, for example, be done by connecting it to a signal.
        # The view can listen to changes:
        cards_model.cards_changed.connect(self.__change_cards)
        # It is completely optional if you want to do it this way, or have some overreaching Player/GameState
        # call the "change_cards" method instead. z

        # Add the cards the first time around to represent the initial state.
        self.__change_cards()

    def __change_cards(self):
        # Add the cards from scratch
        self.scene.clear()
        for i, card in enumerate(self.model.cards):
            # The ID of the card in the dictionary of images is a tuple with (value, suit), both integers
            graphics_key = (card.get_value(), card.suit)
            renderer = self.back_card if self.model.flipped() else self.all_cards[graphics_key]
            c = CardItem(renderer, i)

            # Shadow effects are cool!
            shadow = QGraphicsDropShadowEffect(c)
            shadow.setBlurRadius(10.)
            shadow.setOffset(5, 5)
            shadow.setColor(QColor(0, 0, 0, 180))  # Semi-transparent black!
            c.setGraphicsEffect(shadow)

            # Place the cards on the default positions
            c.setPos(c.position * self.card_spacing, 0)
            self.scene.addItem(c)

        self.update_view()

    def update_view(self):
        scale = (self.viewport().height()-2*self.padding)/313
        self.resetTransform()
        self.scale(scale, scale)
        # Put the scene bounding box
        self.setSceneRect(-self.padding//scale, -self.padding//scale,
                          self.viewport().width()//scale, self.viewport().height()//scale)

    def resizeEvent(self, painter):
        # This method is called when the window is resized.
        # If the widget is resize, we gotta adjust the card sizes.
        # QGraphicsView automatically re-paints everything when we modify the scene.
        self.update_view()
        super().resizeEvent(painter)

    # You can remove these events if you don't need them.
    #def mouseDoubleClickEvent(self, event):
    #    self.model.flip() # Another possible event. Lets add it to the flip functionality for fun!


class PotView(QLabel):
    def __init__(self, pot: pm.PotModel):
        super().__init__()
        self.pot = pot
        self.pot.value_changed.connect(self.update_value)
        self.update_value()

    def update_value(self):
        self.setText(f'Pot: {self.pot.value}')


class PlayerView(QGroupBox):
    def __init__(self, player: pm.PlayerModel):
        super().__init__(player.name)

        vbox = QVBoxLayout()
        self.money = QLabel()
        vbox.addWidget(self.money)
        hand = CardView(player.hand)
        vbox.addWidget(hand)
        self.setLayout(vbox)

        # Connect signals:
        self.player = player
        self.player.money_changed.connect(self.update_money)
        self.update_money()  # Trigger an initial refresh
    
    def update_money(self):
        self.money.setText(f'Money: {self.player.money}')
        

class GameView(QWidget):
    def __init__(self, game: pm.TexasHoldEm):
        super().__init__()
        self.game = game

        self.game.final_winner.connect(self.final_winner)
        self.game.round_winner.connect(self.round_winner)

        # Player box [Player, Player]
        playerbox = QHBoxLayout()
        for player in game.players:
            playerbox.addWidget(PlayerView(player))

        # Button box [Active player; Pot; Bet; Fold; Call]
        buttonbox = QVBoxLayout()
        self.active_player = QLabel()
        self.game.active_player_changed.connect(self.update_active_player)
        buttonbox.addWidget(self.active_player)
        buttonbox.addWidget(PotView(game.pot))

        bet = QPushButton('Bet')
        bet.clicked.connect(self.place_bet)
        buttonbox.addWidget(bet)

        fold = QPushButton('Fold')
        fold.clicked.connect(game.fold)
        buttonbox.addWidget(fold)
        
        call = QPushButton('Call')
        call.clicked.connect(game.call)
        buttonbox.addWidget(call)

        # Table box [Table, Button box]
        tablebox = QHBoxLayout()
        tablebox.addWidget(CardView(game.table))
        tablebox.addLayout(buttonbox)

        # Full view: [Player box; Table box]
        vbox = QVBoxLayout()
        vbox.addLayout(playerbox)
        vbox.addLayout(tablebox)
        self.setLayout(vbox)

        self.update_active_player()
        self.show()

    def update_active_player(self):
        self.active_player.setText("{}'s turn".format(self.game.active_player.name))

    def place_bet(self):
        amount, did_input = QInputDialog.getInt(self, 'Placing bet', 'Bet', 1, self.game.minimum_bet(), self.game.active_player.money, 1)
        if did_input:
            self.game.bet(amount)

    def round_winner(self, winner: int, hand_type: cl.HandType):
        msg = QMessageBox(self)
        if winner == -1:
            msg.setText('Draw with {}'.format(hand_type.name))
        else:
            msg.setText('{} won with {}'.format(self.game.players[winner].name, hand_type.name))
        msg.exec_()

    def final_winner(self, winner: int):
        msg = QMessageBox(self)
        msg.setText('{} won. Well done.'.format(self.game.players[winner].name))
        msg.exec_()
