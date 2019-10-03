s = str(input())
import re

from re import split
res=""
tmp = split('([^a-zA-Z0-9])',s)
result = []



for a in tmp[:]:
    if a.isalnum():
        result.append(a)
result[0] = result[0].lower()
for i in range(1,len(result)):
    result[i] = result[i].capitalize()
print(''.join(item for item in result))
