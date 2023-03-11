from PyQt5.QtWidgets import QApplication
import pokerview as pv
import pokermodel as pm
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = pm.TexasHoldEm(['Mikael', 'Hugo'])
    view = pv.GameView(game)
    app.exec_()
