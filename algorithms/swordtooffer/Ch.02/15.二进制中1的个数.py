def number_of_bits(number):
    '''
    输入一个证书，输出该数二进制表示中1的个数
    :return:
    '''
    count = 0
    if number < 0:
        number = number & 0xffffffff
    while number:
        count += 1
        number = (number - 1) & number
    return count