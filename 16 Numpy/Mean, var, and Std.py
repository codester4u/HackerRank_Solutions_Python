import numpy

n,m=list(map(int,input().split()))
A=[]
for i in range(n):
    A.append(list(map(int,input().split())))
A=numpy.array(A)
print(numpy.mean(A,axis=1))
print(numpy.var(A,axis=0))
print(round(numpy.std(A),11))
