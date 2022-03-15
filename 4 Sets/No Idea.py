n,m=input().split()
array=[int(i) for i in input().split()]
A=set([int(i) for i in input().split()])
B=set([int(i) for i in input().split()])
happiness=0
for i in array:
    if i in A:
        happiness+=1
    if i in B:
        happiness-=1
print(happiness)
