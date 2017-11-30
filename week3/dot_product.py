def dot_product(a,b):
    res = 0 
    a.sort()
    b.sort()

    for i in range(len(a)):
        res += a[i] * b[len(a)-i-1]
    return res

if __name__ == '__main__':
    b = list(map(int, raw_input().split()))
    a = list(map(int, raw_input().split()))
    n = int(raw_input())
    print(dot_product(a,b))
    #a = list(map(int, raw_input().split())
  # b = list(map(int, raw_input().split())
    #print(dot_product(a, b))
