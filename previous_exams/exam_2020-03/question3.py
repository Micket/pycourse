from __future__ import annotations
from enum import Enum, unique
from collections import defaultdict
from typing import List


@unique
class StorageType(Enum):
    Standard = 0
    Cold = 1
    Freezer = 2


@unique
class StorageUnit(Enum):
    pieces = 0
    kg = 1
    liter = 2
    cans = 3


class InventoryItem(object):
    def __init__(self, name: str, storage: StorageType = StorageType.Standard, unit: StorageUnit = StorageUnit.pieces):
        self.name = name
        self.storage = storage
        self.unit = unit

    def __repr__(self):
        return f"{self.name} ({self.storage.name}) [{self.unit.name}]"

    def __hash__(self):
        return hash(self.name)

    def __lt__(self, other: InventoryItem):
        return self.name < other.name


class Inventory(object):
    def __init__(self, name: str):
        self.name = name
        self.items = defaultdict(int)

    def add(self, item: InventoryItem, amount: float or int = 1):
        if amount < 0:
            raise ValueError

        self.items[item] += amount

    def remove(self, item: InventoryItem, count: float or int = 1):
        if item not in self.items:
            raise KeyError

        if self.items[item] - count < 0:
            raise ValueError

        self.items[item] -= count

    def __repr__(self):
        text = "{}: ".format(self.name)
        for item in sorted(self.items):
            text += str(item) + ": " + str(self.items[item]) + ", "
        text = text.rstrip(", ")
        return text


inv = Inventory('Kitchen')
print(inv)
beans = InventoryItem('Beans', unit=StorageUnit.cans)
rice = InventoryItem('Rice', unit=StorageUnit.kg)
egg = InventoryItem('Egg', storage=StorageType.Cold)
inv.add(beans, 4)
inv.add(rice, 0.5)
inv.add(egg, 6)
print(inv)

inv.remove(beans, 2)
inv.remove(egg, 1)
print(inv)

try:
    inv.remove(InventoryItem('Concrete'))
    print(f'Wow, did we store concrete in the {inv.name}!')
except KeyError:
    print(f'No concrete in the {inv.name}!')

try:
    inv.remove(egg, 10)
    print(f'Wow, plenty of eggs in the {inv.name}!')
except ValueError:
    print(f'Not enough eggs in the {inv.name}!')
