import sys
from cardsmodel import HandModel
from cardsview import CardsView
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# Creating a small demo window to work with, and put the card_view inside:
class TestWindow(QWidget):
    def __init__(self, hand):
        super().__init__()
        box = QVBoxLayout()
        card_view = CardsView(hand, card_spacing=50)
        box.addWidget(card_view)
        button = QPushButton("Flip!")
        button.clicked.connect(hand.flip)
        box.addWidget(button)
        self.setLayout(box)

qt_app = QApplication(sys.argv)
hand = HandModel()
player_view = TestWindow(hand)
player_view.show()
qt_app.exec_()
