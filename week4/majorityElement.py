


def majorityElement():
    
    a = [1,2,3,4,1,1]
    new =[]
    for i in a:
       if a.count(i) > 2:

           new.append(i)


    n = len(set(new))
    
    return n
   # print(len(set(new)))
    #return len(set(new))


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if majorityElement(a, 0, n) != -1:
        print(1)
   else:
        print(0)

#print(majorityElement())
