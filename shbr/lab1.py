def valid_number(numb):
    return 1 <= numb <= pow(10, 5)


def valid_numbers(n, m):
    return 1 <= n * m <= pow(10, 6)


n = input()
m = input()
q = input()

if valid_number(n) or valid_numbers(n, m):

    map = {}
    for i in range(int(n)):
        lst = []
        for j in range(int(m)):
            lst[j] = j
