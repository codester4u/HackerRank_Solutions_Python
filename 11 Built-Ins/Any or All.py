n,A=int(input()),[int(i) for i in input().split()]
print(all([x > 0 for x in A]) and any([str(x) == str(x)[::-1] for x in A]))
