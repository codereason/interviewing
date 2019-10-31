'''

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''
def addBinary(a,b):
    carry = 0
    if not b: return a
    if not a: return b
    length_diff, min_len,max_len = len(a) - len(b), min(len(a), len(b)),max(len(a),len(b))

    res = ""
    a = a[::-1]
    b = b[::-1]
    if length_diff>0:
        b+="0"*length_diff
    else:
        length_diff = -1*(length_diff)
        a+="0"*length_diff
    print(length_diff,a,b)
hhn
    for i in range(max_len):
        tmp = int(a[i]) + int(b[i]) + carry
        carry = 0
        if tmp >= 2:
            carry = 1
            tmp=tmp%2
        res += str(tmp)
    print(res)
    if carry==1:
        res+=str(carry)

    # if length_diff == 0:
    #     res += str(carry)
    # elif length_diff > 0:
    #     res += a[min_len:] + str(carry)
    # else:
    #     res += b[min_len:] + str(carry)

    return res[::-1]

if __name__ == '__main__':
    a,b = "1","111"
# "11110"
    # a = "1010", b = "1011"
    print(addBinary(a,b))

