import abc

class Node(metaclass=abc.ABCMeta):
    escapes = [('&', '&amp;'),
               ('"', '&quot;'),
               ("'", '&apos;'),
               ('>', '&gt;'),
               ('<', '&lt;')]

    def __init__(self, name):
        self.name = name

    def escaped_name(self):
        tmp = self.name
        for orig, esc in self.escapes:
            tmp = tmp.replace(orig, esc)
        return tmp

    @abc.abstractmethod
    def xml_structure(self, indent=0):
        pass

    @abc.abstractmethod
    def __len__(self):
        pass


class Directory(Node):
    def __init__(self, name, nodes):
        super().__init__(name)
        self.nodes = nodes

    def add_node(self, node):
        self.nodes.append(node)

    def xml_structure(self, indent=0):
        output = ' ' * indent + '<directory name="{}">\n'.format(self.escaped_name())
        for node in self.nodes:
            output += node.xml_structure(indent + 4)
        output += ' ' * indent + '</directory>\n'
        return output

    def __len__(self):
        return sum([len(n) for n in self.nodes]) + 1

class File(Node):
    def __init__(self, name, binary=True):
        super().__init__(name)
        self.binary = binary

    def xml_structure(self, indent=0):
        return ' '*indent + '<file name="{}" binary="{}" />\n'.format(self.escaped_name(), 'yes' if self.binary else 'no')

    def __len__(self):
        return 1

# test_question4.py:
some_files = [File('Important data.dat'), File('"Quotes" & jokes.txt', False)]
some_code = [File('important_python_code.py', False), File('cheat_sheet.py', False)]
code_dir = Directory('Code', some_code)
root = Directory('Directories can also have "escaped" characters', some_files)
root.add_node(code_dir)
print(root.xml_structure())
print("Total number of nodes in tree is {}".format(len(root)))
