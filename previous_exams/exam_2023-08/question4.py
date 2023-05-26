import abc

class HTMLElement(metaclass=abc.ABCMeta):
    def __init__(self, style=None):
        self.style = style

    @abc.abstractmethod
    def __str__(self):
        pass

    def style_string(self):
        # Note: I wasn't picky about whether or not an extra space is added here or not
        # This just makes calling code a bit neater; either approach is fine.
        return f' style="{self.style}"' if self.style is not None else ''


class TextElement(HTMLElement):
    def __init__(self, element, style=None):
        super().__init__(style)
        if type(element) == str or issubclass(type(element), TextElement):
            self.element = element
        else:
            raise TypeError("TextElement's element must be str or TextElement")

    @abc.abstractmethod
    def tag_name(self):
        pass

    def __str__(self):
        s = self.style_string()
        t = self.tag_name()
        return f'<{t}{s}>{self.element}</{t}>'


class BoldText(TextElement):
    def tag_name(self):
        return 'b'


class ItalicText(TextElement):
    def tag_name(self):
        return 'i'


class Link(HTMLElement):
    def __init__(self, url, element, style=None):
        super().__init__(style)
        self.url = url
        self.element = element

    def __str__(self):
        s = self.style_string()
        return f'<a href="{self.url}"{s}>{self.element}</a>'


class Paragraph(HTMLElement):
    def __init__(self, elements, style=None):
        super().__init__(style)
        self.elements = elements

    def __str__(self):
        contents = ' '.join([str(element) for element in self.elements])
        s = self.style_string()
        return f'<p{s}>{contents}</p>'


class Body(HTMLElement):
    def __init__(self, elements, style=None):
        super().__init__(style)
        self.elements = elements

    def __str__(self):
        contents = '\n    '.join([str(element) for element in self.elements])
        s = self.style_string()
        return f'<body{s}>\n    {contents}\n</body>'


p0 = Paragraph(["Text can be", ItalicText("cursive,"), BoldText("bold"), "or",
                ItalicText(BoldText("both"), style="color:red")])
print("first paragraph as HTML:")
print(p0)
print()
p1 = Paragraph([BoldText("Chalmers"), Link('https://www.chalmers.se', "link", 'color:blue')])
print("second paragraph as HTML:")
print(p1)
print()
body = Body([p0, p1])
print("whole body as HTML:")
print(body)
