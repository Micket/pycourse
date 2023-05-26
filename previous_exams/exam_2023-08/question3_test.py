# Test code
x = Interval(1., 3.)
y = Interval(-4., 5.)
z = Interval(-10., 0.)
v = y.union(z)

print('x overlaps z =', x.overlaps(z))
print('y overlaps z =', x.overlaps(y))
print('v =', v)
print('-x = ', -x)
print('-y = ', -y)
print('-z = ', -z)

print('x + y =', x+y)
print('x - y =', x-y)
print('z - x =', z-x)

print('x * y =', x*y)
print('z * y =', z*y)
print('y * y =', y*y)

print('float(x) =', float(x))
print('float(y) =', float(y))
print('float(z) =', float(z))

# v = y.union(Interval(4,7))  # should raise your exception

