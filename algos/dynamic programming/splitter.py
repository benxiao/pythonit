import string


if __name__ == '__main__':
    import sys
    argv = sys.argv
    assert len(argv) == 3
    _, infilename, outfilename = argv
    with open(infilename) as infile:
        doc = infile.read()
    doc = doc.upper()
    doc = "".join(x if x in string.ascii_uppercase else " " for x in doc)
    words = doc.split()
    words = [x for x in words if len(x) > 1]
    with open(outfilename, "w") as outfile:
        outfile.write("\n".join(words)+"\n")