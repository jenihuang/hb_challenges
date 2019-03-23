"""Merge sort.

    >>> merge_sort([3, 5, 10, 2, 1, 9, 7, 6, 4, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


def merge_sort(lst):
    """Divide and conquer: reduce to lists of 0-1 items, then recombine."""
    if len(lst) < 2:
        return lst
    else:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)


def merge(lst1, lst2):
    """given two sorted lists, combine them"""

    results = []
    i = 0
    j = 0

    while i <= len(lst1) - 1 and j <= len(lst2) - 1:

        if lst1[i] < lst2[j]:
            results.append(lst1[i])
            i += 1
        else:
            results.append(lst2[j])
            j += 1

    if i == len(lst1):
        results.extend(lst2[j:])
    else:
        results.extend(lst1[i:])

    return results


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AWESOME WORK!\n")
