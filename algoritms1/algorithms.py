def find_max_number(word):
    ans = ''
    anscnt = 0

    # O (n ^ 2)
    for i in range(len(word)):
        nowcnt = 0
        for j in range(len(word)):
            if word[i] == word[j]:
                nowcnt += 1
        if nowcnt > anscnt:
            ans = word[i]
            anscnt = nowcnt

    # O (n * k) => O (n)
    for now in set(word):
        nowcnt = 0
        for j in range(len(word)):
            if now == word[j]:
                nowcnt += 1
        if nowcnt > anscnt:
            ans = now
            anscnt = nowcnt

    print(ans)



if __name__ == '__main__':
    seq = [1,2,3,4,5]
    for el in range(seq, -1):
        print(seqel)
