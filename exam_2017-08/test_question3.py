k = np.array([[1,2,3],[4,5,6],[7,8,9]])
g = np.array([[1,0],[0,-1],[-1,1]])
x = np.array([1,0,2,3,0])

a = ConstrainedMatrix(k, g)
v = a.dot_product(x) 
print(v) # should be [10, 16, 22, -1, 2]
