import sys


def min_dot_product(A, B):
    A.sort()
    B.sort(reverse=True)

    return sum([x[0] * x[1] for x in zip(A, B)])


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    A = [int(_) for _ in sys.stdin.readline().split()]
    B = [int(_) for _ in sys.stdin.readline().split()]

    print min_dot_product(A, B)
