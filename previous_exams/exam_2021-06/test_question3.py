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

# 3 quintillion floats!
w = RepeatedList([3.14, 2.72, 1.41], 1000000000000000000)
assert len(w) == 3000000000000000000
print(w)
print(w[2999999999999999999])
