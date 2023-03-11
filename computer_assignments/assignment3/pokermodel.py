import cardlib as cl
import abc
from PyQt5.QtCore import QObject, pyqtSignal


class PotModel(QObject):
    value_changed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__value = 0

    @property
    def value(self):
        return self.__value

    def __iadd__(self, money: int):
        self.__value += money
        self.value_changed.emit()
        return self

    def clear(self):
        self.__value = 0
        self.value_changed.emit()


class CardModel(QObject):
    cards_changed = pyqtSignal()

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
        self.cards_changed.emit()

    def clear(self):
        self.cards.clear()
        self.cards_changed.emit()

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
        self.cards_changed.emit()

    def clear(self):
        self.cards.clear()
        self.__flipped = True
        self.cards_changed.emit()

    def flipped(self):
        return self.__flipped

    def flip(self):
        self.__flipped = not self.__flipped
        self.cards_changed.emit()

    def reveal(self):
        self.__flipped = False
        self.cards_changed.emit()


class PlayerModel(QObject):
    money_changed = pyqtSignal()
    
    def __init__(self, name: str, money: int = 100):
        super().__init__()
        self.name = name
        self.money = money
        self.current_bet = 0
        self.hand = HandModel()

    def bet(self, money: int):
        self.money -= money
        self.current_bet += money
        self.money_changed.emit()

    def win(self, money: int):
        self.money += money
        self.current_bet = 0
        self.money_changed.emit()


class TexasHoldEm(QObject):
    active_player_changed = pyqtSignal()
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

        self.active_player.hand.flip()
        self._next_player()

    def _next_player(self):
        self.active_player.hand.flip()
        self.player_turn = (self.player_turn + 1) % len(self.players)
        self.active_player.hand.flip()
        self.active_player_changed.emit()

    @property
    def active_player(self) -> PlayerModel:
        return self.players[self.player_turn]

    def fold(self):
        self._next_player()
        self.active_player.win(self.pot.value)
        self._next_round()

    def minimum_bet(self) -> int:
        return 1 + (self.min_bet - self.active_player.current_bet)

    def bet(self, money: int):
        self.active_player.bet(money)
        self.min_bet = self.active_player.current_bet
        self.pot += money
        self._next_player()

    def call(self):
        max_bet = max([player.current_bet for player in self.players])
        diff = max_bet - self.active_player.current_bet
        self.active_player.bet(diff)
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
