def solution(number):
    lst = []

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            lst.append(i)

    return sum(lst)


def spin_words(sentence):
    words = sentence.split(" ")
    res = []
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
        res.append(word)

    result = ' '.join(map(str, res))
    return result


def narcissistic(value):
    result = 0
    i = len(str(value))
    for numb in str(value):
        result += int(numb) ** i

    return value == result


def open_or_senior(data):
    lst = []
    for values in data:
        if values[0] >= 55 and values[1] > 7:
            lst.append("Senior")
        else:
            lst.append("Open")

    return lst


def nb_year(p0, percent, aug, p, years=0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years


def rgb(r, g, b):
    res = rgb_to_hex(r)
    res += rgb_to_hex(g)
    res += rgb_to_hex(b)


def rgb_to_hex(rgb):
    if rgb < 0:
        return '00'
    elif rgb > 255:
        return 'FF'
    return '%02X' % rgb


def digital_root(n, res=0):
    if n > 0:
        res += n % 10
        return digital_root(n // 10, res)
    if res >= 10:
        return digital_root(res // 10, res % 10)
    else:
        return res


if __name__ == '__main__':
    print(digital_root(493193))
