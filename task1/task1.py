from itertools import cycle
n, m = int(input()), int(input())
sk = cycle(range(1, n+1))
def func(it, num):
    left = next(it)
    right = 0
    while right != 1:
        yield left
        for _ in range(num-2):
            next(it)
        right = next(it)
        left = right
print(*func(sk, m), sep='')
