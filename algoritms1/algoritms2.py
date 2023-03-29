def find_max(seq):
    ans = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > ans:
            ans = seq[i]
    return ans

if __name__ == '__main__':
    print(find_max([1,2,3,4,5]))
