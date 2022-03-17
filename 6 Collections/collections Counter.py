from collections import Counter
X=int(input())
sizes=[int(i) for i in input().split()]
sizes=Counter(sizes)
#print(sizes)
N=int(input())
earnings = 0
for customer in range(N):
    size, x_i = map(int,input().split())
    if size in sizes and sizes[size] > 0:
        sizes[size] -= 1
        earnings += x_i
print(earnings)
