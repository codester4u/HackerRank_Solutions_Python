from numpy import *

n,m=list(map(int,input().split()))
A=[]
for i in range(n):
    x=list(map(int,input().split()))
    A.append(x)
A=array(A)
print(transpose(A))
print(A.flatten())
