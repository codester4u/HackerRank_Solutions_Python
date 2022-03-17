from collections import deque
N=int(input())
d=deque()
for i in range(N):
    x=input().split()
    if x[0]=="append":
        d.append(x[1])
    elif x[0]=="appendleft":
        d.appendleft(x[1])
    elif x[0]=="pop":
        d.pop()
    elif x[0]=="popleft":
        d.popleft()
print(*d)
