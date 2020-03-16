---
header-includes:
        - \usepackage[left=1.9cm, right=1.9cm, top=1.5cm, bottom=1.9cm]{geometry}
---

# Question 3: A simple inventory (6p)

You want to use Python to help you keep track of your groceries and decide to create a class representing an inventory.

Part A (3p)
-------------
**Task:**  Thinking on how to implement this you come to the conclusion that you need a helper class to represent the items in the inventory, and therefore
need to create the class `InventoryItem` with the following constructor:

`InventoryItem(name: str, storage: StorageType, unit: StorageUnit)`

Here `StorageType` must be an `Enum` type and have at least the choices `Standard`, `Cold` and `Freezer`. `StorageUnit` must be an `Enum` type and have at
least the choices `kg`, `liter`, `cans` and `pieces`.


For `InventoryItem` implement the following:

* Make the constructor have `Standard` as the default `StorageType` and `pieces` as the default `StorageUnit`
* A method for `<`: Compare on the item name
* A suitable method to be able to use `print()` on an object of this type

Part B (2.5p)
-----------

**Task:** Implement the class `Inventory`.

Implement the following methods for `Inventory`:

*  The constructor should take the inventory name as a parameter
* `add(item: InventoryItem, amount: int or float)` - should add a new item to the inventory, or add to the amount of the item if it is already present
* `remove(item: InventoryItem, amount: int or float)` - should remove the given amount from an existing item in the inventory
* A suitable method to be able to use `print()` on an object of this type


*Hint: If you want to use an `InventoryItem` as a key, you need to implement the `__hash__` method for that class.
       The name can be used as a key for hash()-ing on!*


Part C (0.5p)
-----------
**Task:** Add code to `Inventory` so that the `add` and `remove` methods raise suitable errors if a to small or large `amount` is given, or the
item to remove is not found in the inventory.

See example on next page!

\newpage

**Example code:**
```python
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
```

**Example output (your format can be different!):**
```python
Kitchen: 
Kitchen: Beans (Standard) [cans]: 4, Egg (Cold) [pieces]: 6, Rice (Standard) [kg]: 0.5
Kitchen: Beans (Standard) [cans]: 2, Egg (Cold) [pieces]: 5, Rice (Standard) [kg]: 0.5
No concrete in the Kitchen!
Not enough eggs in the Kitchen!
```

\newpage

