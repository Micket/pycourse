def read_recipe(filename)
    quantities = dict()
    with open(filename) as file:
        for line in file:
            if ':' not in line: continue
            ingredient, quantity = line.split(':')
            quantities[ingredient.strip().lower()] = float(quantity)

def read_calorie_data(filename):
    cal_db = dict()
    with open(filename) as file:
        for line in file:
            ingredient, calories = line.strip().split(',')
            value = calories.rstrip('kJ')
            unit = calories[:len(value)].strip()
            scale = 1000 if 'k' in unit else 1
            db[ingredient.strip().lower()] = float(value) * scale
    return cal_db

def compute_calories(cal_db, recipe):
    c = 0
    for ingredient, quantity in recipe:
        c += db[ingredient] * quantity
    return c


cal_db = read_calorie_data('calorie_data.txt')
recipe = read_recipe('apple_pie.txt')
calories = compute_calories(cal_db, recipe)
print('The apple pie has {calories} calories')
