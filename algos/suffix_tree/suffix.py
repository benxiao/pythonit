class Suffix:
    def __init__(self, text, offset):
        self.text = text
        self.offset = offset

    def __len__(self):
        return len(self.text) - self.offset

    def __getitem__(self, index):
        return self.text[index]

    def __str__(self):
        return self.text[self.offset:]

    __repr__ = __str__

    def __iter__(self):
        for i in range(self.offset, len(self.text)):
            yield self.text[i]

    def __lt__(self, other):
        for ch1, ch2 in zip(self, other):
            if ch1 != ch2:
                return ord(ch1) < ord(ch2)
        return len(self) < len(other)

    



if __name__ == '__main__':
    text = "banana"
    suffixes = []
    for i in range(len(text)):
        suffixes.append(Suffix(text, i))
    print(suffixes[0])
    print(suffixes[1])
    print(suffixes[0] < suffixes[1])
    suffixes.sort()
    print(suffixes)

