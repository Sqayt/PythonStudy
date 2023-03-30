def find_max(seq):
    # ans = seq[0]
    # for i in range(1,len(seq)):
    #     if seq[i] > ans:
    #         ans = seq[i]
    # return ans

    ans = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[ans]:
            ans = i
    return seq[ans]


def find_max2(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range(2, len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]

    return max1, max2


def find_min(seq):
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (ans == -1 or seq[i] < ans):
            ans = seq[i]

    return ans


def short_words(words):
    min_len = len(words[0])
    for word in words:
        if len(word) < min_len:
            min_len = len(word)
    ans = []
    for word in words:
        if len(word) == min_len:
            ans.append(word)

    return ' '.join(ans)


# RLE
def rle(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    last_sym = s[0]
    last_pos = 0
    ans = []
    for i in range(1, len(s)):
        if s[i] != last_sym:
            ans.append(pack(last_sym, i - last_pos))
            last_pos = i
            last_sym = s[i]
    ans.append(pack(s[last_pos], len(s) - last_pos))

    return ''.join(ans)


def easypeasy(s):
    last_sym = s[0]
    ans = []
    for i in range(1, len(s)):
        if s[i] != last_sym:
            ans.append(last_sym)
            last_sym = s[i]
    ans.append(last_sym)

    return ''.join(ans)


if __name__ == '__main__':
    print(short_words(['aba', 'ab', 'c', 'd', 'e']))
