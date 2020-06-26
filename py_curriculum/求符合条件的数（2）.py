import math
def fac(n):
    i = 2
    divisor_num = 1
    while i <= n // 2:
        if n % i == 0:
            divisor_num += i
        i += 1

    return divisor_num

def isPrime(n):
    if n == 1:
        return False
    square_root = int(math.sqrt(n))
    for i in range(2, square_root + 1):
        if n % i == 0:
            return False
    return True

def getNumberPairs(n):
    try:
        temp = [i for i in range(4, n + 1) if isPrime(i) != 1]
        for i in temp:
            j = fac(i)
            #
            if j not in temp or i == j:
                continue
            if fac(j) == i:
                print('{}-{}'.format(i, j))
                temp.remove(i)
    except Exception as e:
        raise e

getNumberPairs(3000)
