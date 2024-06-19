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

