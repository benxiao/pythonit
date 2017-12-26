from getBWT import manber_myers

CHAR2INT = {"$": 0, "A": 1, "C": 2, "G": 3, "T": 4}
INT2CHAR = ["$", "A", "C", "G", "T"]
CHARSET_LENGTH = len(CHAR2INT)

if __name__ == '__main__':
    # file
    # with open("bwt1000001.txt") as fp:
    #     text = fp.read()
    text = "AAAACTAAAACTTACT"
    testcases = ["A"]

    if not text.endswith("$"):
        text += "$"

    # with open("shortpatterns.txt") as fp:
    #     testcases = [x.rstrip() for x in fp]

    # encode testcases
    for i, s in enumerate(testcases):
        testcases[i] = [CHAR2INT[x] for x in s]

    # find suffix array
    suffix = manber_myers(text)

    # encode bwt str
    last = [CHAR2INT[text[s - 1]] for s in suffix]
    length = len(last)

    # construct frequency table
    length = len(last)
    freq = [0] * CHARSET_LENGTH
    for i in last:
        freq[i] += 1

    # construct rank table
    rank = [0] * CHARSET_LENGTH
    for i in range(1, CHARSET_LENGTH):
        rank[i] = rank[i - 1] + freq[i - 1]

    # construct occurrences table
    occurrences = []
    row = [0] * CHARSET_LENGTH
    occurrences.append(row)
    for ch in last:
        row = row[:]
        row[ch] += 1
        occurrences.append(row)

    # test each pattern
    for pat in testcases:
        found, sp, ep = True, 0, len(text) - 1
        for ch in reversed(pat):
            sp = rank[ch] + occurrences[sp][ch]
            ep = rank[ch] + occurrences[ep][ch] - 1 + (last[ep] == ch)
            if sp > ep:
                found = False
                print("early break")
                break

        times = (ep - sp + 1) if found else 0
        pat_str = "".join(INT2CHAR[x] for x in pat)
        print("Pattern {} appears {} times".format(pat_str, times))
        if found:
            suffixes = []
            for i in range(sp, ep+1):
                suffixes.append(suffix[i])
            suffixes.sort()
            for s in suffixes:
                print(s)
        print(end='\n'*2)
