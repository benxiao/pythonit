from merge_sort import merge_sort
from ht import HashTableQP

if __name__ == '__main__':
    import sys
    argv = sys.argv
    assert len(argv) == 3
    _, input_file, out_file = argv
    ht = HashTableQP()
    with open(input_file) as infp:
        for line in infp:
            word = line.rstrip('\n')
            if word in ht:
                ht[word] += 1
            else:
                ht[word] = 1

    items = [(w, ht[w]) for w in ht]
    merge_sort(items, key=lambda x: x[0])
    with open(out_file, "w") as outfp:
        for w, f in items:
            outfp.write("{} {}\n".format(w, f))




