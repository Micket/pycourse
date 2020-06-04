from __future__ import annotations
from datetime import date

class InvalidPerson(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Person(object):
    def __init__(self, firstname: str, lastname: str, born: date, dead: date = None):
        self.first = firstname
        self.last = lastname
        self.born = born
        self.dead = dead
        self._parents = set()
        self._spouse = None
        self._children = set()

    def add_parent(self, parent: Person):
        self._parents.add(parent)

    def add_child (self, child: Person):
        if child in self._children:
            raise InvalidPerson("You can only add a child once!")
        self._children.add(child)

    def set_spouse(self, spouse: Person):
        self._spouse = spouse

    def __eq__(self, other: Person):
        return self.first == other.first and self.last == other.last and self.born == other.born

    def count_descendants(self) -> int:
        count = len(self._children)
        for c in self._children:
            count += c.count_descendants()
        return count

    def __lt__(self, other: Person):
        return (self.last, self.first, self.born) < (other.last, other.first, other.born)

    def __hash__(self):
        return hash((self.last, self.first, self.born))

    def __repr__(self):
        s = f"{self.first} {self.last} ({self.born}"
        if self.dead:
            s += f" - {self.dead}"
        s += ")"
        return s

    def show(self):
        print(self)
        if self._parents:
            print(" Parents:", ", ".join([str(c) for c in self._parents]))
        if self._spouse:
            print(" Spouse:", self._spouse)
        if self._children:
            print(" Children:", ", ".join([str(c) for c in self._children]))


class Family(object):
    def __init__(self, parent1: Person, parent2: Person = None):
        self.parents = [parent1]
        if parent2:
            if parent1 == parent2:
                raise InvalidPerson("You can't add a parent as a child to the same family!")
            self.parents.append(parent2)
            parent1.set_spouse(parent2)
            parent2.set_spouse(parent1)

    def add_child(self, child: Person):
        for p in self.parents:
            if child == p:
                raise InvalidPerson("A person can only occur once in a Family!")
            if child.born <= p.born:
                raise InvalidPerson("A child must be younger than its parent!")
            p.add_child(child)
            child.add_parent(p)

p1 = Person("Glenn", "Svensson", date(1990, 10, 21))
p2 = Person("Ada", "Andersson", date(1992, 5, 11))
p3 = Person("Lotta", "Svensson", date(2013, 9, 17))
p4 = Person("Knut", "Andersson", date(2015, 8, 29))

p5 = Person("Lovisa", "Eriksson", date(1927, 7, 3), date(2003, 2, 9))

print(p1, p2, sep=", ")
print(p3, p4, sep=", ")

f1 = Family(p5)
f1.add_child(p2)

f2 = Family(p2, p1)
f2.add_child(p3)
f2.add_child(p4)


p1.show()
p3.show()

print(p5, "Descendants:", p5.count_descendants())

try:
    f3 = Family(p1, p1)
except InvalidPerson as e:
    print(e)

try:
    f2.add_child(p2)
except InvalidPerson as e:
    print(e)

try:
    f2.add_child(p3)
except InvalidPerson as e:
    print(e)

try:
    f2.add_child(p5)
except InvalidPerson as e:
    print(e)
