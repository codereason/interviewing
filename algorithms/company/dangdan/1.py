



def is_cross(s1,s2,s3):
    if len(s1) + len(s2) != len(s3):
        return 0
    m, n = len(s1), len(s2)

    arr = [[False]*(n+1) for _ in range(m+1)]
    arr[0][0]=True
    for i in range(1,m+1):
        arr[i][0] = arr[i-1][0] and s1[i-1] == s3[i-1]
    for j in range(1,n+1):
        arr[0][j] = arr[0][j-1] and s2[j-1] == s3[j-1]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            arr[i][j] = (arr[i-1][j] and s1[i-1]==s3[i+j-1]) or (arr[i][j-1] and s2[j-1]==s3[i+j-1])
    return arr[-1][-1]


if __name__ == '__main__':
    strings = input().split(" ")
    s1, s2, s3 = strings[0], strings[1], strings[2]
    crs = is_cross(s1,s2,s3)
    print(1 if crs else 0)