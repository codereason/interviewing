'''
题目描述
ONU是一种新型桌游，一副牌有若干种花色，总共N张，且每种花色的牌的张数一样。现在每次给定N，M，表示这幅总共N张的牌至少有M种花色，请问这副牌可能的花色有多少种？

输入

共一行，两个整数N，M。（1<=N<=1012，0<=M<=1012）

输出

一个整数，表示可能的花色种数。

样例输入

30 14

样例输出

2

Hint

可能有15或者30种花色，所以总共两种花色数。
--------------------- 
作者：阿木寺 
来源：CSDN 
原文：https://blog.csdn.net/amusi1994/article/details/82855791 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''


def func(N, M):
    return len([a for a in range(1, N + 1) if N % a == 0 and a >= M])


if __name__ == '__main__':
    N, M = map(int, input("").split())
    print(func(N, M))
