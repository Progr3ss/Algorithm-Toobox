

def huge_fib(n,m):
    

    if (n == 0):
        
        return 0 

    fib = {0:0, 1:1}
    mod = {0:0, 1:1}

    i = 2 

    while True: 

        fib.setdefault(i,mod.get(i-1) + mod.get(i-2))
        mod.setdefault(i,fib.get(i) % m)


        if(mod[i-1] == 0 and mod[i] ==1):
            break

        i = i +1
    remainder = n %(i-1)
    return fib.get(remainder) % m


if __name__ == '__main__':
    n,m = map(int, raw_input().split())
    print(huge_fib(n,m))
