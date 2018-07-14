import math

@profile
def isArmstrongNum(n):

    n_list = list(str(n))
    k = len(n_list)
    result = sum([int(x) ** k for x in n_list])
    if result == n:
        return True
    else:
        return False

@profile
def isArmstrongNum2(n):

    a = []
    t = n
    while t > 0:
        a.append(t % 10)
        t = math.floor(t / 10)
    k = len(a)
    return sum([x ** k for x in a]) == n


if __name__ == '__main__':
    for x in range(100, 999):
        if isArmstrongNum(x):
            pass
