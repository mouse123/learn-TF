import numpy as np

a = np.array([1, 2, 3])  # Create a rank 1 array
print (type(a))            # Prints( "<type 'numpy.ndarray'>"
print (a.shape)           # Prints( "(3,)"
print (a[0], a[1], a[2])   # Prints( "1 2 3"
a[0] = 5                 # Change an element of the array
print (a)                  # Prints( "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
print (b.shape )                    # Prints( "(2, 3)"
print (b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

A = np.zeros((2,2))
print (A)

B = np.ones((1,2))
print (B)

C = np.full((2,2), 7)
print (C)

D = np.eye(2)
print (D)

E = np.random.random((1,1,3))
print (E)

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

b = a[:, 1:2]

print (a)
print (a.shape)
print (b)
print (b.shape)
print (a[0, 1])
b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]
print (a[0, 1])