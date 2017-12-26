"""
* * * key index counting * * *
"""


# [(int, object)]
def sort_by_integer(array):
    """
    complexity: O(n)
    :param array: [(int, object)]
    :return: array: [(int, object)] sorted in ascending order
    """
    l = len(array)
    max_freq = max([x for x, _ in array])
    print(max_freq)
    count = [0] * (max_freq + 2)
    aux = [None] * l
    for i, _ in array:
        print(i)
        count[i+1] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for item in array:
        aux[count[item[0]]] = item
        count[item[0]] += 1

    return aux
