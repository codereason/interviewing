zhaimport sys


def check(list):
    flag = True
    for num in list:
        if num < 0:
            return False
    return True


if __name__ == '__main__':
    line = sys.stdin.readline().strip().split(' ')
    n = int(line[0])

    data = list(map(int, sys.stdin.readline().strip().split(' ')))
    print(data)
    if check(data) is False:

        for i in range(len(data)):
            if data[i] < 0:
                data[i] = 0 - data[i]

        print(sum(data))