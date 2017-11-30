


def maximizingValue():
    
    dic = {3:50,60:20,100:50,120:30}
    #dic.update({v:w})

    for k,v in dic.iteritems():
        print(k,v)
         
    return dic

if __name__ == '__main__':
   # v,w= (raw_input().split() )
  # w = int(input())
 
    print(maximizingValue())
