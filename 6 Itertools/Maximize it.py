from itertools import product
K,M=list(map(int,input().split()))
l1=[]
for i in range(K):
    x=[abs(int(i)) for i in input().split()][1:]
    #print(x)
    l1.append(x)
results = map(lambda x: sum(i**2 for i in x)%M, product(*l1))
print(max(results))