import time

start = time.time()


def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo


# CHAR2INT = {"$":0, "A":1, "C":2, "G":3, "T":4}
# INT2CHAR = ["$", "A", "C", "G", "T"]


UTF_8_SIZE = 256
CHAR2INT = {chr(i): i for i, ch in enumerate(range(UTF_8_SIZE))}
INT2CHAR = [chr(i) for i in range(UTF_8_SIZE)]


if __name__ == '__main__':

    import sys

    argv = sys.argv
    assert len(argv) == 2
    _, infile = argv
    with open(infile) as fp:
        text = fp.read()

    #text = "hd-$-__dnnhtoeesmsdn______uellbbvbhbiltcettlvhraeaeh_iAoKtDgoEiau_su_i_smner"
    CHARSET_LENGTH = len(CHAR2INT)

    # encode to integer
    last = [CHAR2INT[ch] for ch in text]

    # construct frequency table
    length = len(last)
    freq = [0] * CHARSET_LENGTH
    for i in last:
        freq[i] += 1

    # construct rank table
    rank = [0] * CHARSET_LENGTH
    for i in range(1, CHARSET_LENGTH):
        rank[i] = rank[i - 1] + freq[i - 1]

    # construct occurences table
    occurrences = [0] * length
    temp = [0] * CHARSET_LENGTH
    for i, c in enumerate(last):
        occurrences[i] = temp[c]
        temp[c] += 1

    # lf mapping
    pos = 0
    i = 0
    temp = []
    # (O(n)) length of the string
    while pos < length:
        # find the char index based on rank table (O(1))
        # as the charset length is constant
        ###################################
        cur = bisect(rank, i) - 1

        # cur = None
        # for j, r in enumerate(rank):
        #     if i < r:
        #         cur = j - 1
        #         #print("assignment", cur)
        #         break
        # if cur is None:
        #     cur = CHARSET_LENGTH - 1
        ###################################
        temp.append(cur)
        i = occurrences[i] + rank[last[i]]
        pos += 1

    with open("originalstring.txt", "w") as fp:
        fp.write("".join(INT2CHAR[i] for i in reversed(temp)))
    print(time.time() - start)
