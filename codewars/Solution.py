import re
from math import sqrt

def to_camel_case(text):
    word_array = re.split(r"[-_]", text)
    lst = [word_array[0]]
    for i in range(1, len(word_array)):
        if not word_array[i].istitle():
            lst.append(word_array[i].title())
        else:
            lst.append(word_array[i])

    return ''.join(lst)

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True

    maximum_dividor = sqrt(num) + 1

    for i in range(2, maximum_dividor):
        if num % i == 0:
            return False

    return True

def count_bits(n):
    res = bin(n)

    count = 0
    for i in res:
        if i == '1':
            count += 1

    return count

def move_zeros(lst):
    result = []
    count = 0
    for el in lst:
        if el == 0:
            count += 1
        else:
            result.append(el)
    for el in range(0, count):
        result.append(0)

    return result


def score(values):
    from collections import Counter
    count = Counter(values)
    score = 0
    for value, amount in count.items():
        if value > 6:
            raise ValueError("Invalid dice value")
        if value == 1:
            value = 10
        trip, left = divmod(amount, 3)
        score += trip * value * 100
        if value in (10, 5):
            score += left * value * 10

    return score


def loop_size(node):
    current = node
    i = 1
    setattr(current, "visited", True)
    setattr(current, "n", i)
    while not hasattr(current.next, "visited"):
        current = current.next
        setattr(current, "visited", True)
        i += 1
        setattr(current, "n", i)
    n = (i + 1) - current.next.n

    return n


if __name__ == '__main__':
    print(
        score(
            [5, 1, 3, 4, 1]
        )
    )