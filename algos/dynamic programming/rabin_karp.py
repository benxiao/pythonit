R = 256
Q = 10262821 # prime


def hash(s):
    H = 0
    for ch in s:
        H = (H * R) % Q
        H = (H + ord(ch))
    return H

def rabin_karp(src, pat):
    h_pat = hash(pat)
    h_src = hash(src[:len(pat)])
    rm = pow(R, len(pat)-1, Q)
    i = 0
    n = len(src) - len(pat)
    while i <= n:
        if (h_pat == h_src) and match(src, pat, i):
            return i

        if i == n:
            break

        h_src = (h_src - rm * ord(src[i])) % Q # pop first character
        h_src = (h_src * R + ord(src[i+len(pat)])) % Q # add a more character
        i += 1

    return -1

def match(src, pat, i):
    for j in range(len(pat)):
        if src[j+i] != pat[j]:
            return False
    return True




if __name__ == '__main__':
    src = "So you compare two hash values and since they are different, \
    you move forward. Now you reach to second substringin string.  \
    Here is where the fun begins. We can calculate the hash of this string without rehashing everything. \
    As you can see, the window has moved forward only by dropping one character and adding another:"
    pat = "dropping"
    print(rabin_karp(src, pat))
    print(src.find(pat))
