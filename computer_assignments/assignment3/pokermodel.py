import cardlib as cl
import abc
from PyQt5.QtCore import QObject, pyqtSignal


class PotModel(QObject):
    new_pot = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.value = 0

    def __iadd__(self, money: int):
        self.value += money
        self.new_pot.emit()
        return self

    def clear(self):
        self.value = 0
        self.new_pot.emit()


class CardModel(QObject):
    new_cards = pyqtSignal()

    @abc.abstractmethod
    def __iter__(self):
        pass

    @abc.abstractmethod
    def flipped(self):
        pass


class TableModel(CardModel):
    def __init__(self):
        super().__init__()
        self.cards = []

    def add_card(self, card: cl.PlayingCard):
        self.cards.append(card)
        self.new_cards.emit()

    def clear(self):
        self.cards.clear()
        self.new_cards.emit()

    def flipped(self):
        return False

    def __iter__(self):
        return iter(self.cards)


class HandModel(cl.Hand, CardModel):
    def __init__(self):
        cl.Hand.__init__(self)
        CardModel.__init__(self)
        self._flipped = True

    def __iter__(self):
        return iter(self.cards)

    def add_card(self, card: cl.PlayingCard):
        super().add_card(card)
        self.new_cards.emit()

    def clear(self):
        self.cards.clear()
        self._flipped = True
        self.new_cards.emit()

    def flipped(self):
        return self._flipped

    def flip(self):
        self._flipped = not self._flipped
        self.new_cards.emit()

    def reveal(self):
        self._flipped = False
        self.new_cards.emit()


class PlayerModel(QObject):
    new_money = pyqtSignal()
    
    def __init__(self, name: str, money: int = 100):
        super().__init__()  # Necessary for signals to work!
        self.name = name
        self.money = money
        self.current_bet = 0
        self.hand = HandModel()

    def bet(self, money: int):
        self.money -= money
        self.current_bet += money
        self.new_money.emit()

    def win(self, money: int):
        self.money += money
        self.current_bet = 0
        self.new_money.emit()


class TexasHoldEm(QObject):
    new_active_player = pyqtSignal()
    round_winner = pyqtSignal(int, cl.HandType)
    final_winner = pyqtSignal(int)

    def __init__(self, player_names: list):
        super().__init__()
        self.players = [PlayerModel(name) for name in player_names]
        self.table = TableModel()
        self.pot = PotModel()
        self.player_turn = 0
        self.min_bet = 0
        self.deck = None
        self._next_round()

    def _next_round(self):
        for i, player in enumerate(self.players):
            if player.money == 0:
                other = 0 if i == 1 else 1
                self.final_winner.emit(other)
                return

        self.deck = cl.StandardDeck()
        self.deck.shuffle()
        self.pot.clear()
        self.min_bet = 0
        self.table.clear()
        for player in self.players:
            player.hand.clear()
            for _ in range(2):
                player.hand.add_card(self.deck.draw())

        self.active_player().hand.flip()
        self._next_player()

    def _next_player(self):
        self.active_player().hand.flip()
        self.player_turn = (self.player_turn + 1) % len(self.players)
        self.active_player().hand.flip()
        self.new_active_player.emit()

    def active_player(self) -> PlayerModel:
        return self.players[self.player_turn]

    def fold(self):
        self._next_player()
        self.active_player().win(self.pot.value)
        self._next_round()

    def minimum_bet(self) -> int:
        return 1 + (self.min_bet - self.active_player().current_bet)

    def bet(self, money: int):
        self.active_player().bet(money)
        self.min_bet = self.active_player().current_bet
        self.pot += money
        self._next_player()

    def call(self):
        max_bet = max([player.current_bet for player in self.players])
        diff = max_bet - self.active_player().current_bet
        self.active_player().bet(diff)
        self.pot += diff

        if len(self.table.cards) == 0:
            for _ in range(3):
                self.table.add_card(self.deck.draw())
            self._next_player()
        elif len(self.table.cards) < 5:
            self.table.add_card(self.deck.draw())
            self._next_player()
        else:
            for player in self.players:
                player.hand.reveal()

            best_hands = [player.hand.best_poker_hand(self.table.cards) for player in self.players]
            if best_hands[0] == best_hands[1]:  # draw!
                # Give back bet to each player:
                for player in self.players:
                    player.win(player.current_bet)
                self.round_winner.emit(-1, best_hands[0].hand_type)
            else:
                winner = 0 if best_hands[1] < best_hands[0] else 1
                self.players[winner].win(self.pot.value)
                for player in self.players:
                    player.win(0)  # TODO: could be expanded to deal with cases when winner didn't win entire pot.
                self.round_winner.emit(winner, best_hands[winner].hand_type)
            self._next_round()
