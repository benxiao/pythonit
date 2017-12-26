from sort import merge_sort
from suffix import Suffix
text = "GCGCCCCGTGCGCCCCC$"


def suffix_array(text):
    l = len(text)
    sa = list(range(l))
    rank = [ord(x) for x in text]
    merge_sort(sa, key=lambda x: rank[x])
    k = 1
    while k < l:
        print(k)
        added_rank = [0] * l
        for i in sa:
            if i+k < l:
                added_rank[i] = rank[i+k]
        merge_sort(sa, key=lambda x: (rank[x], added_rank[x]))
        temp =[0] * l
        for i in range(1, l):
            if rank[sa[i]] == rank[sa[i-1]] and added_rank[sa[i]] == added_rank[sa[i-1]]:
                temp[sa[i]] = temp[sa[i-1]]
            else:
                temp[sa[i]] = temp[sa[i-1]] + 1
        temp, rank = rank, temp
        k *= 2
    return sa



if __name__ == '__main__':
    text = "googol$"
    sa = suffix_array(text)
    print(sa)
    print("".join(text[s] for s in sa))
    # # sa = suffix_array(text)
    # # print(sa)
    # # for i in sa:
    # #     print(Suffix(text, i))
    # import time
    #
    # start = time.time()
    # # sa = suffix_array(text)
    # text = open("bwt1000001.txt").read()
    # sa = suffix_array(text)
    # print(time.time() - start)

