S=input()
s=input()
N,n=len(S),len(s)
flag=0
for i in range(N):
    if s==S[i:i+n]:
        print(f"({i}, {i+n-1})")
        flag=1
if flag==0:
    print("(-1, -1)")
