# Test
nd = NormalDistribution(sigma=0.25, offset=0.25)
print(repr(nd))
print(f'nd(0.3) = {nd(0.3)}')
print(f'nd(1.0) = {nd(1.0)}')
print(f'nd.integrate(0., 0.5) = {nd.integrate(0., 0.5)}')
print([nd.random() for _ in range(10)])  # expect numbers near 0 to 0.5

print()

ud = UniformDistribution(width=0.5, offset=0.25)  # covers the interval 0 to 0.5
print(repr(ud))
print(f'ud(0.3) = {ud(0.3)}')
print(f'ud(1.0) = {ud(1.0)}')
print(f'ud.integrate(0., 0.5) = {ud.integrate(0., 0.5)}')
print([ud.random() for _ in range(10)])  # expect numbers within 0 to 0.5

