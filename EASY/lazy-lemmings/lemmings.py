"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    >>> furthest(7, [0, 6])
    3

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""
    # find max distance between all cafes and integer divide by 2

    distances = set()
    distances.add(cafes[0])
    distances.add(num_holes - cafes[-1] - 1)

    for i in range(1, len(cafes)):
        distances.add((cafes[i] - cafes[i - 1]) // 2)

    return max(distances)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
