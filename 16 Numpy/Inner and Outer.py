import numpy

A=numpy.array(list(int(i) for i in input().split()))

B=numpy.array(list(int(i) for i in input().split()))
print(numpy.inner(A,B))
print(numpy.outer(A,B))
