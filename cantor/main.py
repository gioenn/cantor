import sys
import math

'''Q -> N (cantor pairing function)'''
def q_encode(x, y):
    x = z_encode(x)-1
    y = z_encode(y)-1
    res = (x+y)*(x+y+1)/2 + y + 1
    return int(res)

''' N -> Q (cantor inverse pairing function)'''
def q_decode(n):
    if n <= 0:
        raise ValueError("input must be a natural number")
    n = int(n) - 1
    w = math.floor((math.sqrt(8*n + 1)-1)/2)
    t = (w*w + w)/2
    y = int(n-t)
    x = int(w-y)
    return z_decode(x+1), z_decode(y+1)

''' Z -> N '''
def z_encode(z):
    z = int(z)
    if z >= 0:
        return z*2 + 1
    else:
        return -z*2

''' N -> Z '''
def z_decode(n):
    if n <= 0:
        raise ValueError("input must be a natural number")
    n = int(n)
    if n % 2 == 0:
        return -n//2
    else:
        return int(math.floor(n/2))
