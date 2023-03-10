# Test
db = Bijection()
db2 = Bijection((('a', 1), ('b', 2)))

db.add(('a', 1))
db.add(('b', 2))
db.add(('c', 3))

assert db.map_forward('b') == 2
assert db.map_backward(1) == 'a'

for a, b in db2:
    print(a, '<-->', b)

print()
print(db)
db.delete(second=3)
print(db)
db.delete(first='a')
print(db)
