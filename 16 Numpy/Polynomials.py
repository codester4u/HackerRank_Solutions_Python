import numpy

A=numpy.array([float(i) for i in input().split()])
print(numpy.polyval(A,int(input())))
