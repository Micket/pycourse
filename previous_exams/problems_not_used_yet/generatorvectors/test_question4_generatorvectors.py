# Test code:
def test_vector(v):
    print("Vector:", v)
    print("Length:", len(v))
    print("At pos 1 and 3:", v[1], v[3])
    print("Collected:", v.collect())

    print("Adding 3")
    v2 = 3 + v
    print("Vector:", v2)
    print("Length:", len(v2))
    print("At pos 1 and 3:", v2[1], v2[3])
    print("Collected:", v2.collect())

    print("and mutliplying by 0.5")
    v3 = v2 * 0.5
    print("Vector:", v3)
    print("Length:", len(v3))
    print("At pos 1 and 3:", v3[1], v3[3])
    print("Collected:", v3.collect())
    print("")

cv = ConstantVector(3.5, 5)
test_vector(cv)

lv = LinspaceVector(0.5, 1.5, 5)
test_vector(lv)

from math import sqrt
fv = FunctionVector(sqrt, 5)
test_vector(fv)

