#coding=utf-8
def count(N):
    '''
    讨论1000的阶乘结尾有几个0的问题，就被转换成了1到1000所有这些数的质因数分解式有多少个5的问题。
    :param N:
    :return:
    '''


def trailing_zero_num(n):
    num = 0

    while True:
        n = int(n / 5)
        if n == 0:
            break
        num = num + n

    return num

if __name__ == '__main__':
    print(trailing_zero_num(100))