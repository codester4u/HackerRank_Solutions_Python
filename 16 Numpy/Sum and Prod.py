import numpy

n,m=map(int,input().split())
A=[]
for i in range(n):
    x=list(map(int,input().split()))
    A.append(x)
        
su=numpy.sum(A,axis=0)
print(numpy.prod(su))
