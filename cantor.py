import sys
import math

def cantor_pairing(x, y):
    return (x+y)*(x+y+1)/2 + y

def cantor_pairing_inv(n):
    w = math.floor((math.sqrt(8*n + 1)- 1)/2)
    t = (w*w + w)/2
    y = int(n-t)
    x = int(w-y)
    return (x, y)

def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        print(cantor_pairing_inv(n))
    elif len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print(cantor_pairing(x, y))
    else:
        print("invalid input")

if __name__ == "__main__":
    main()
