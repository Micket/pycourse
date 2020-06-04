p1 = Person("Glenn", "Svensson", date(1990, 10, 21))
p2 = Person("Ada", "Andersson", date(1992, 5, 11))
p3 = Person("Lotta", "Svensson", date(2013, 9, 17))
p4 = Person("Knut", "Andersson", date(2015, 8, 29))

p5 = Person("Lovisa", "Eriksson", date(1927, 7, 3), date(2003, 2, 9))

print(p1, p2, p3, p4, sep=", ")

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
