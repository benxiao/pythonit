from collections import deque

PRIME = 319
BASE = 128


def rabinKarp(source, target):
    # validate inputs
    if len(source) < len(target):
        return -1

    target_hash = 0
    for ch in target:
        target_hash = (target_hash * BASE + ord(ch)) % PRIME

    # only read from target_hash from now on
    # constant used to remove the first character from the hash
    RM = pow(BASE, len(target) - 1, PRIME)

    # generating initial hash
    rolling_hashing = 0
    # use queue to keep track of a segment of characters that are hashed
    q = deque()
    gen0 = iter(source)
    for i in range(len(target)):
        current_char = next(gen0)
        rolling_hashing = (rolling_hashing * BASE + ord(current_char)) % PRIME
        q.append(current_char)

    if target_hash == rolling_hashing:
        check = True
        for ch0, ch1 in zip(target, q):
            if ch0 != ch1:
                check = False
                break
        if check:
            return 0

    for i in range(len(source) - len(target)):
        current_char = next(gen0)
        removed_char = q.popleft()
        rolling_hashing = ((rolling_hashing - ord(removed_char) * RM) * BASE + ord(current_char)) % PRIME
        q.append(current_char)
        if rolling_hashing == target_hash:
            check = True
            for ch0, ch1 in zip(target, q):
                if ch0 != ch1:
                    check = False
                    break
            if check:
                return i + 1
    return -1


if __name__ == '__main__':
    print(rabinKarp("abbbc", "abb"))
