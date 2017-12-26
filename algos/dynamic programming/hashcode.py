INTEGER_MAX = 2 ** 32


def hash(text, hash=0):
    h = hash
    for ch in text:
        h = (31 * h + ord(ch)) % INTEGER_MAX
    return h


def hash2(text, hash=0):
    h = hash
    for ch in text:
        h = (19 * h + ord(ch)) % INTEGER_MAX
    return h


if __name__ == '__main__':
    print(hash("a9090908"))
    print(hash2("a9090908"))