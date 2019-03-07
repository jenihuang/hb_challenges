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

    >>> furthest_optimized(7, [0, 6])
    3

    >>> furthest_optimized(3, [0, 1, 2])
    0

    >>> furthest_optimized(3, [2])
    2

    >>> furthest_optimized(3, [0])
    2

    >>> furthest_optimized(6, [2, 4])
    2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""
    # make a sorted list with num_holes items
    # replace cafes with flag
    # use two loops to loop through every index until it reaches True save in a list
    # loop through every reverse list and save in same list
    # return max of that list
    # runtime O(n^2)

    holes = [i for i in range(num_holes)]
    results = []
    for num in cafes:
        holes[num] = True

    for i in range(holes):
        steps = 0
        if holes[i] != True:
            steps += 1
            for i in range(holes - i):
                if holes[i] == True:
                    results.append(steps)
                else:
                    steps += 1


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
