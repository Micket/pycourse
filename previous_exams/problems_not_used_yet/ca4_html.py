import abc

class HTMLElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass


class TextElement(HTMLElement):
    def __init__(self, element):
        if type(element) == str or issubclass(element, TextElement):
            self.element = element
        else:
            raise TypeError("BoldText can only take str or TextElements")

    @abc.abstractmethod
    def tag_name(self):
        pass

    def __str__(self):
        return '<{}>{self.element}</{0}>'.format(self.tag())


class BoldText(TextElement):
    def tag_name(self):
        return 'b'


class CursiveText(TextElement):
    def tag_name(self):
        return 'i'


class Paragraph(TextElement):
    def tag(self):
        return 'p'


def Link(HTMLElement):
    def __init__(self, link, element):
        self.link = link
        self.element = element

    def __str__(self):
        return f'<a href="{self.link}">{self.element}</a>'
