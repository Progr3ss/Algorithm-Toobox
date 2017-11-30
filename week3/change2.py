

def change(m):
    coins = [1,5,10]
    d = coins.pop()
    i = 0
    while m:
        if d > m:
            d = coins.pop()
        else:
            print(m)
            m -= d 
            i += 1 
    return i


if __name__ == '__main__':
    
    m = int(input())
    print(change(m))
           
