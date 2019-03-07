def OnlyOnce(str):
    dict = {}
    for char in str:
        if char not in dict:
            dict[char]=1
        else:dict[char]+=1
    for char in str:
        if dict[char]==1:

            return char

if __name__ == '__main__':
    str = "abaccdeff"
    print(OnlyOnce(str))