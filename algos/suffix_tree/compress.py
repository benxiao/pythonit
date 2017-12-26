a = "googol$"

def compress(text):
    prev = text[0]
    l = len(text)
    count = 1
    temp = []
    for i in range(1, l):
        cur = text[i]
        if cur != prev:
            temp.append(prev)
            temp.append(str(count))
            count = 1
            prev = cur

        else:
            count += 1

    return "".join(temp)

print(compress(a))




def decompress(compressed):
    i = 0
    j = 0
