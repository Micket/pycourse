import os

# Part A
def read_recipe(filename):
    recipe = dict()
    with open(filename) as file:
        for line in file:
            if line.startswith('#'): continue
            ingredient, quantity = line.split('=')
            recipe[ingredient.strip().lower()] = float(quantity)
    return recipe

# Part B
def read_calorie_data(filename):
    cal_db = dict()
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if len(line) == 0: continue # Skip empty lines
            ingredient, calories = line.split(':')
            value = calories.rstrip('kJcal')
            unit = calories[:len(value)].strip()
            scale = 1000 if 'k' in unit else 1
            if 'J' in unit:
                scale *= 4.184
            cal_db[ingredient.strip().lower()] = float(value) * scale
    return cal_db

# Part C
def compute_calories(cal_db, recipe):
    c = 0
    for ingredient, quantity in recipe.items():
        c += cal_db[ingredient] * quantity
    return c

# Part A
recipe = read_recipe('recipes/apple_pie.txt')
print(recipe)

# Part B
cal_db = read_calorie_data('calorie_data.txt')
print(cal_db)

# Part C
calories = compute_calories(cal_db, recipe)
print(calories)

# Part D
for name in os.listdir('recipes/'):
    recipe = read_recipe(f'recipes/{name}')
    calories = compute_calories(cal_db, recipe)
    print(f'{name} has {calories:.1f} calories')
    
