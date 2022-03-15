A=[int(i) for i in input().split()]
N=int(input())
res=[]
flag=1
for i in range(N):
    res.append([int(i) for i in input().split()])
for i in res:
    for j in i:
        if j not in A:
            flag=0
            break
if flag==0:
    print("False")
else:
    print("True")    
