T=int(input())
for _ in range(T):
    m=int(input())
    A=[int(i) for i in input().split()]
    n=int(input())
    B=[int(i) for i in input().split()]
    flag=1
    for i in A:
        if i not in B:
            flag=0
            break
    if flag==1:
        print("True")
    else:
        print("False")
