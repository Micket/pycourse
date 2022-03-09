import abc


class TUIWidget(abc.ABC):
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows

    @abc.abstractmethod
    def render(self) -> list:
        return 

    def show(self):
        for line in self.render():
            print(line)



class TextField(TUIWidget):
    def __init__(self, columns, rows, text=''):
        super().__init__(columns, rows)

    def set_text(self, new_text):
        self.text = text

    def render(self):
        lines = []
        for n in range(rows):
            lines.append(self.text[(self.columns*n):(self.columns*(n+1))])
        return lines


# A bit tricky.. but it would be nice to have something here
#class Equalizer(TUIWidget):
#    def __init__(self, columns, max_value, data):
#        self.max_value = max_value
#        self.data = data
#
#    def set_data(self, data):
#        self.data = data
#
#    def render(self):
#        block = numpy.zeros(self.columns, self.rows)
#        block[np.array(self.data) / max_value * self.columns]
#        rendered_data = [[' ' for _ in self.rows] for _ in self.columns]
#        return [''.join(row) for row in rows]


class CheckerBoard(TUIWidget):
    def render(self):
        # Create a big board that is to big and just trim it
        # We could be more clever, but lets keep this simple
        bw = ('█ ' * self.columns)[:self.columns]
        wb = (' █' * self.columns)[:self.columns]
        lines = []
        for i in range(self.rows):
            lines.append(bw)
            lines.append(wb)
        return lines[:self.rows]


class Box(TUIWidget):
    def __init__(self, widget):
        super().__init__(self, widget.columns + 2, widget.rows + 2)
        self.widget = widget

    def render(self):
        lines = self.widget.render()
        for i, line in enumerate(lines):
            padding = widget.columns - len(line)
            lines[i] = '|' + line + ' '*padding + '|'
    
        horizontal_border = '+' + '-'*widget.columns + '+'
        lines.append(horizontal_border)
        lines.prepend(horizontal_border)
        return lines


class GroupBox(Box):
    def __init__(self, name, widget):
        super().__init__(self, widget)
        self.name = name

    def render(self):
        lines = super().render()
        # Just replace the top horizontal bar
        before = '+-['
        after = ']' + '-'*(self.columns-len(self.name)-3) + '+'
        lines[0] = '+' + before + self.name + after + '+'


