x = RepeatedList([1,2,3], 3)
assert len(x) == 9
assert len(x.tolist()) == 9
print(x)
for i, v in enumerate(x):
    print(f'{i}: {v}')
print(x.tolist())

y = RepeatedList([4,5,6], 0)
assert len(y) == 0
for v in y:
    assert False  # Should not occur
print(y)

z = RepeatedList([], 3)
assert len(y) == 0
print(z)
for v in z:
    assert False  # Should not occur
