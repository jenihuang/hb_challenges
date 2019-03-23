"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    # O(n) time and space?

    # results = []
    # index_a = 0
    # index_b = 0

    # while index_a <= (len(a) - 1) and index_b <= (len(b) - 1):
    #     if a[index_a] < b[index_b]:
    #         results.append(a[index_a])
    #         index_a += 1

    #     else:
    #         results.append(b[index_b])
    #         index_b += 1

    # if index_a < len(a) - 1:
    #     results.extend(a[index_a:])
    # else:
    #     results.extend(b[index_b:])

    # return results

    if not a and not b:
        return []
    elif not a:
        return b
    elif not b:
        return a
    else:
        if a[-1] > b[-1]:
            largest = a.pop()
            results = sort_ab(a, b)
            results.append(largest)
            return results
        else:
            largest = b.pop()
            results = sort_ab(a, b)
            results.append(largest)
            return results


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n")
