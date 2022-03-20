import re

A = re.findall(r'(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})(?=[bcdfghjklmnpqrstvwxyz])', input().strip(), re.IGNORECASE)

if A:
    for i in A:
        print(i)
else:
    print(-1)
