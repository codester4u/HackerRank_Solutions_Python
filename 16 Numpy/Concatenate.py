import numpy

N,M,P=list(map(int,input().split()))
A,B=[],[]
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(M):
    B.append(list(map(int,input().split())))
A,B=numpy.array(A),numpy.array(B)
print(numpy.concatenate((A,B),axis=0))
