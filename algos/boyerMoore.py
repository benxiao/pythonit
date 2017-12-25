text = "WASHINGTON — In the Obama administration’s last days, some White House officials scrambled to spread information about Russian efforts to undermine the presidential election — and about possible contacts between associates of President-elect Donald J. Trump and Russians — across the government. Former American officials say they had two aims: to ensure that such meddling isn’t duplicated in future American or European elections, and to leave a clear trail of intelligence for government investigators."


def boyerMoore(source, target, start=None, end=None):
    # how many characters to jump over
    jump_table = [-1] * 256
    for i, ch in enumerate(target):
        jump_table[ord(ch)] = i

    # last possible index len(source)-len(target)
    i = start or 0
    if end:
        end_index = end - len(target)  # maybe buggy
    else:
        end_index = len(source) - len(target) + 1

    assert end_index > i

    while i < end_index:  # endIndex not reachable
        skip = 0
        print(source[i:i + len(target)])
        for j in reversed(range(len(target))):  # compare source and target string in reverse order
            if target[j] != source[j + i]:
                ch = source[j + i]
                if ord(ch) < 256:
                    skip = max(j - jump_table[ord(ch)], 1)  # jump at least one
                else:
                    # unicode characters assume they are not in the target
                    skip = j + 1
                break
        if not skip:
            return i
        i += skip
        print("jump over {} characters".format(skip))

    return -1


if __name__ == '__main__':
    print(boyerMoore(text, "Donald J. Trump"))
