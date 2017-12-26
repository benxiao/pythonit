def kic_index(array, rank):
    assert len(array) > 0
    l_array = len(array)
    l_charset = max(l_array, 256) # utf-8
    temp_array = [None] * l_array

    count_array = [0] * (l_charset + 1)
    # contruct frequency array
    for s in array:
        count_array[rank[s] + 1] += 1

    # construct cumulative index array
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    # sort the array by one digit
    # result copyed to temp_array
    for i, s in enumerate(array):
        temp_array[count_array[rank[s]]] = array[i]
        count_array[rank[s]] += 1

    return temp_array


def kic_sort(char_array):
    assert len(char_array) > 0
    l_array = len(char_array)
    l_charset = 256  # utf-8
    temp_array = [None] * l_array
    count_array = [0] * (l_charset + 1)
    # contruct frequency array
    for s in char_array:
        count_array[ord(s) + 1] += 1

    # construct cumulative index array
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    # sort the array by one digit
    # result copyed to temp_array
    for i, s in enumerate(char_array):
        temp_array[count_array[ord(s)]] = char_array[i]
        count_array[ord(s)] += 1

    return temp_array


if __name__ == '__main__':
    print(kic_sort(['c', 'b','g','e','d','f','a']))




