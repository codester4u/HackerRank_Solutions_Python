import numpy

A=[int(i) for i in input().split()]
A=numpy.array(A)
print(numpy.reshape(A,(3,3)))
