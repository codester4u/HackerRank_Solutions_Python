import numpy

N,M=map(int,input().split())
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))
A=numpy.array(A)
x=numpy.min(A,axis=1)
print(max(x))
