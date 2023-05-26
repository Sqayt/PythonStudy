# native O (n^2)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_new(n):
    F = [-1] * (n + 1)
    F[0] = 0
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]

    return F[n]


if __name__ == '__main__':
    print(fib_new(10))