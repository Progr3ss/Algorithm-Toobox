#!/usr/bin/env python2

import sys

def recursive_binary_search(L, low, high, key):
    if low >  high:
        return -1
    mid = low + ((high - low) / 2)
    if key == L[mid]:
        return mid
    elif key < L[mid]:
        return recursive_binary_search(L, low, mid - 1, key)
    else:
        return recursive_binary_search(L, mid + 1, high, key)


def iterative_binary_search(L, low, high, key):
    while low <= high:
        mid = low + ((high - low) / 2)
        if key == L[mid]:
            return mid
        elif key < L[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

if __name__ == '__main__':
    A = [int(_) for _ in sys.stdin.readline().split()][1:]
    B = [int(_) for _ in sys.stdin.readline().split()][1:]

    for b in B:
        print iterative_binary_search(A, 0, len(A) - 1, b),
