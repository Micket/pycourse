from __future__ import annotations

class Person(object):
    def __init__(self, firstname: str, lastname: str, born: int, dead: int = None):
        self.first = firstname
        self.last = lastname
        self.born = born
        self.dead = dead
        self._parents = {"Mother": None, "Father": None}
        self._spouse = None
        self._children = set()

    def set_mother(self, mother: Person):
        self._parents["Mother"] = mother

    def set_father(self, father: Person):
        self._parents["Father"] = father

    def set_spouse(self, spouse: Person):
        self._spouse = spouse

    def add_child (self, child: Person):
        self._children.add(child)

    def __eq__(self, other: Person):
        return self.first == other.first and self.last == other.last and self.born == other.born

    def __lt__(self, other: Person):
        return (self.last, self.first, self.born) < (other.last, other.first, other.born)

    def __hash__(self):
        return hash((self.last, self.first, self.born))

    def __repr__(self):
        s = f"{self.first} {self.last} ({self.born}"
        if self.dead:
            s += f"-{self.dead}"
        s += ")"
        return s

    def show(self):
        print(self)
        if self._parents["Mother"]:
            print(" Mother:", self._parents["Mother"])
        if self._parents["Father"]:
            print(" Father:", self._parents["Father"])
        if self._spouse:
            print(" Spouse:", self._spouse)
        if self._children:
            print(" Children:", ", ".join([str(c) for c in self._children]))

class Family(object):
    def __init__(self, mother: Person, father: Person):
        self.mother = mother
        self.father = father
        mother.set_spouse(father)
        father.set_spouse(mother)

    def add_child(self, child: Person):
        self.mother.add_child(child)
        self.father.add_child(child)
        child.set_mother(self.mother)
        child.set_father(self.father)

p1 = Person("Glenn", "Svensson", 1990)
p2 = Person("Ada", "Andersson", 1992)
p3 = Person("Lotta", "Svensson", 2013)
p4 = Person("Knut", "Andersson", 2015)

p5 = Person("Lovisa", "Eriksson", 1927, 2003)

p1.set_mother(p5)

print(p1, p2, p3, p4, sep=", ")
print(p5)

f1 = Family(p2, p1)
f1.add_child(p3)
f1.add_child(p4)

p1.show()
p3.show()