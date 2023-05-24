cyan = Colour(0, 1, 1)
magenta = Colour(1, 0, 1)
white = Colour.from_hex('#FFFFFF')

if cyan + magenta == white:
    print('{} and {} makes {}'.format(cyan.html(), magent, repr(white))

try:
    Colour(1.1, 0.5, 0.5)
except ValueError:
    print('Value error caught')
