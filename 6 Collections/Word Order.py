from collections import OrderedDict
N=int(input())
d=OrderedDict()
for i in range(N):
    word=input()
    if word in d:
        d[word]+=1
    else:
        d[word]=1
print(len(d));

for k,v in d.items():
    print(v,end = " ");