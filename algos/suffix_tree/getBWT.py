def kic(array, rank):
    assert len(array) > 0
    assert len(array) == len(rank)
    l_array = len(array)
    l_charset = max(l_array, 256)  # utf-8
    print("length:", l_charset)
    temp_array = [None] * l_array

    count_array = [0] * (l_charset + 1)
    # contruct frequency array
    for s in array:
        count_array[rank[s] + 1] += 1

    # construct cumulative index array
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    # sort the array by one digit
    # result copyed to temp_array
    for i, s in enumerate(array):
        temp_array[count_array[rank[s]]] = array[i]
        count_array[rank[s]] += 1
    return temp_array


def manber_myers(text):
    l = len(text)
    sa = list(range(l))
    rank = [ord(x) for x in text]

    sa = kic(sa, rank)
    k = 1
    while k < l:
        # print("rank", rank)
        print(k)
        added_rank = [0] * l
        for i in sa:
            if i + k < l:
                added_rank[i] = rank[i + k]
        # key index counting
        sa = kic(sa, added_rank)
        sa = kic(sa, rank)
        # print(sa)
        temp = [0] * l
        for i in range(1, l):
            if rank[sa[i]] == rank[sa[i - 1]] and added_rank[sa[i]] == added_rank[sa[i - 1]]:
                temp[sa[i]] = temp[sa[i - 1]]
            else:
                temp[sa[i]] = temp[sa[i - 1]] + 1
        rank = temp
        k *= 2
    return sa


if __name__ == '__main__':
    # text = "An_algorithm_such_as_this_must_be_beheld_to_be_believed--Donald_Ervin_Knuth$"
    # sa = manber_myers(text)
    # print(sa)
    # print("".join(text[s-1] for s in sa))



    import time
    import sys
    start = time.time()
    argv = sys.argv
    assert len(argv) == 2
    _, infile = argv
    with open(infile) as fp:
        text = fp.read()
    if not text.endswith("$"):
        text = text + "$"
    sa = manber_myers(text)
    with open("outputbwt.txt", "w") as fp:
        fp.write("".join(text[i - 1] for i in sa))
    print("took "+str(time.time() - start))
