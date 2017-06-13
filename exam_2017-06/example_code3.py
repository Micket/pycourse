from complex import Complex, im

print("Printing")
print(Complex(2,3))
print(Complex(5))
print(Complex(2, -3))

z1 = Complex(2, 3)

print("\nImag / Real")
print(z1.imag())
print(z1.real())

z2 = Complex(4, -2)

print("\nArithmethic")
print(z1 + z2)
print(3 + z1)
print(z1 * z2)
print(5 * z1)
print(z1 * 5)
print(abs(z1))
print(z1 == z1)

print("\nPolar")
r, theta = z1.topolar()
print("r = ", r, "theta = ", theta, "rad")
print(Complex.frompolar(r, theta))

print("\nException")
print(z1 < z1)

