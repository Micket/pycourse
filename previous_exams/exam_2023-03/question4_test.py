# Tests
a = ListDataset('test strings', ["some", "simple", "example", "strings", "are", "always", "easy", "to", "test", "with"])
b = DirectoryDataset('example/poems')
c = DirectoryDataset('example/limericks')
d = SubsetDataset(a, range(1,7,2))
e = RandomDataset('testing')

assert a[1] == "simple"
assert b[2].startswith("There once was a text editor called PyCharm")
assert c.name == "limericks"
assert d.name == "test strings"
assert d[2] == "always"
assert len(c) == 6  # 6 example limericks
assert len(d) == 3
assert len(e.rand()) == 10 and type(e.rand()) == str  q# should be a random 10 character string

print(a.rand())
print(b.rand())
print(c.rand())
