# Uses python3
import sys

def get_change(m):
    #write your code here
    
    result = 0 
    result += int(m/10)
    m = m % 10 
    result += int(m/5)
    m = m % 5
    m = m + result
    return m

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
