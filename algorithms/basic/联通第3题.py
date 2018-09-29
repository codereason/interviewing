def quchong(s):
    b = list(s)
    c = sorted(set(b))
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ret = list(set(c) ^ set(alphabet))
    if len(ret) == 0:return 0
    return ''.join(sorted(ret))


if __name__ == "__main__":
    s = input()

    print(quchong(s))
