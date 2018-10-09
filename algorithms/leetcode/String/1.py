import re
s = "   the  sky      is     blue           "
def rev(s):
    s = s.split()

    return (' '.join(s[::-1]))

print(rev(s))