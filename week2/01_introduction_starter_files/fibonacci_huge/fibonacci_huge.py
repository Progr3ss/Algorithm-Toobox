# Uses python3
import sys
'''
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
'''

def get_fibonacci_huge(n,m):
    if(n == 0):
        return 0

    fib = {0:0, 1:1}
    mod = {0:0,1:1}

    i = 2
    

    while True:

        fib.setdefault(i,mod.get(i-1) + mod.get(i-2))
        mod.setdefault(i,fib.get(i) % m)
        if(mod[i-1] == 0 and mod[i] == 1):
            break
        i = i+1
    remainder = n % (i-1)
    return fib.get(remainder) % m


if __name__ == '__main__':
   # input = sys.stdin.read();
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))
