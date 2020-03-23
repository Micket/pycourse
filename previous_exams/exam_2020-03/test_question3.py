inv = Inventory('Kitchen')
print(inv)
beans = InventoryItem('Beans', unit=StorageUnit.cans)
rice = InventoryItem('Rice', unit=StorageUnit.kg)
egg = InventoryItem('Egg', storage=StorageType.Cold)
inv.add(beans, 4)
inv.add(rice, 0.5)
inv.add(egg, 6)
inv.add(rice, 1)
print(inv)

inv.remove(beans, 2)
inv.remove(egg, 1)
print(inv)

try:
    inv.remove(InventoryItem('Concrete'), 1)
    print(f'Wow, did we store concrete in the {inv.name}!')
except KeyError:
    print(f'No concrete in the {inv.name}!')

try:
    inv.remove(egg, 10)
    print(f'Wow, plenty of eggs in the {inv.name}!')
except ValueError:
    print(f'Not enough eggs in the {inv.name}!')
