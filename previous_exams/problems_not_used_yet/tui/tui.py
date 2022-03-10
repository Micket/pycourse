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

    def set_progress(self, value: float):
        self.progress = value

    def render(self):
        percentage = round(self.progress * 100)
        wblocks = round((self.columns-2) * self.progress)
        bblocks = self.columns - 2 - wblocks
        return ['[' + '#'*wblocks + ' '*bblocks + ']']


class TextField(TUIWidget):
    def __init__(self, columns, rows, text=''):
        super().__init__(columns, rows)
        self.text = text

    def set_text(self, new_text):
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
        before = '+-['
        after = ']' + '-'*(self.widget.columns-len(self.name)-3) + '+'
        lines[0] = before + self.name + after
        return lines


# Test
p = ProgressBar(40)
p.show()
p = ProgressBar(40, 0.1)
p.show()

print()

t = TextField(20, 3, 'Learning Python sure is fun. Even the exam is fun!')
b = Box(t)
b.show()

print()

g = GroupBox("Download", p)
p.set_progress(0.75)
g.show()

