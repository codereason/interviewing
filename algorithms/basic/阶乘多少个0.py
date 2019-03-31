def count(N):
    '''
    讨论1000的阶乘结尾有几个0的问题，就被转换成了1到1000所有这些数的质因数分解式有多少个5的问题。
    :param N:
    :return:
    '''
    count=0
    for i in range(1,N):
        for j in range(1,i):
            if j%5==0:
                count+=1
    return count