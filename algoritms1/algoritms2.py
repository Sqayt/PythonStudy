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

if __name__ == '__main__':
    print(find_max([1,2,3,4,5]))
