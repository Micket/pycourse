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


class ProgressBar(TUIWidget):
    def __init__(self, columns, progress: float=0):
        super().__init__(columns, 1)
        self.progress = progress

    def set_progress(self, progress: float):
        self.progress = progress

    def render(self):
        wblocks = round((self.columns-2) * self.progress)
        bblocks = self.columns - 2 - wblocks
        return ['[' + '#'*wblocks + ' '*bblocks + ']']


class TextField(TUIWidget):
    def __init__(self, columns, rows, text=''):
        super().__init__(columns, rows)
        self.text = text

    def set_text(self, text):
        self.text = text

    def render(self):
        lines = []
        for n in range(self.rows):
            lines.append(self.text[(self.columns*n):(self.columns*(n+1))])
        return lines


class Box(TUIWidget):
    def __init__(self, widget):
        super().__init__(widget.columns + 2, widget.rows + 2)
        self.widget = widget

    def render(self):
        # Using the box drawing unicode characters would have looked nicer: ─│┌┐└┘├┤
        lines = self.widget.render()
        for i, line in enumerate(lines):
            padding = self.widget.columns - len(line)
            lines[i] = '|' + line + ' '*padding + '|'
        horizontal_border = '+' + '-'*self.widget.columns + '+'
        lines.append(horizontal_border)
        lines.insert(0, horizontal_border)  # "prepend"
        return lines


class GroupBox(Box):
    def __init__(self, name, widget):
        super().__init__(widget)
        self.name = name

    def render(self):
        lines = super().render()
        # Just replace the top horizontal bar
        top = lines[0]
        lines[0] = top[:3] + f'[{self.name}]' + top[5+len(self.name):]
        return lines


# Test
p = ProgressBar(22)
p.show()
p = ProgressBar(22, 0.2)  # 10% progress
p.show()
assert p.render() == ['[####                ]']

print()

t = TextField(20, 3, 'Learning Python sure is fun. Even the exam is fun! Not all text fits')
assert t.render()[0] == 'Learning Python sure'
b = Box(t)
b.show()

print()

g = GroupBox("Download", p)
p.set_progress(0.75)
g.show()

print()

g.name = 'Box in a box'
bg = Box(g)
bg.show()

