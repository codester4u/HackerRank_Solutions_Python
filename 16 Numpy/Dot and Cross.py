import numpy

N=int(input())
A,B=[],[]
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))
A,B=numpy.array(A),numpy.array(B)
print(numpy.dot(A,B))
