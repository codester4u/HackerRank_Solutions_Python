S=input()
lower,upper,evendigits,odddigits=[],[],[],[]
for i in S:
    if i.islower(): lower.append(i)
    elif i .isupper(): upper.append(i)
    elif i.isdigit():
        if int(i)%2==0:
            evendigits.append(i)
        else:
            odddigits.append(i)
#print(lower,upper)
lower.sort()
upper.sort()
evendigits.sort()
odddigits.sort()
res=''
for i in lower: res+=i
for i in upper: res+=i
for i in odddigits: res+=i
for i in evendigits: res+=i
print(res)
