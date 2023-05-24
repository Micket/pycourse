class Colour:
    def __init__(self, r, g, b):
         # 1p for exception
        if r < 0 or g < 0 or b < 0 or r > 1 or g > 1 or b > 1:
            raise ValueError("RGB values {} are out of range", (r, g, b))
         # 1p for init
        self.r = r
        self.g = g
        self.b = b

    @staticmethod
    def from_html(v):
        r = int(v[1:3],16)/255
        g = int(v[3:5],16)/255
        b = int(v[5:7],16)/255
        return Colour(r, g, b)

    def __repr__(self):
        return 'Colour(r={},g={},b={})'.format(self.r, self.g, self.b)

    def html(self):
        return '#{:02x}{:02x}{:02x}'.format(int(self.r*255), int(self.g*255), int(self.b*255))

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __hash__(self):
        return hash((self.r, self.g, self.b))

    def __add__(self, other):
        r = min(self.r + other.r, 1)
        g = min(self.g + other.g, 1)
        b = min(self.b + other.b, 1)
        return Colour(r, g, b)


cyan = Colour(0, 1, 1)
magenta = Colour(1, 0, 1)
white = Colour.from_html('#FFFFFF')

if cyan + magenta == white:
    print('{} and {} makes {}'.format(cyan.html(), magenta, repr(white)))

try:
    Colour(1.1, 0.5, 0.5)
except ValueError:
    print('Value error caught')
