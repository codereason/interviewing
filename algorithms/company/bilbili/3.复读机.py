

def is_odd(string):
    return len(string)%2!=0



res = []
s = input().split(" ")


for i in range(len(s)):
    if is_odd(s[i]):
        s[i]=s[i][::-1]
print(" ".join([item for item in s]))

