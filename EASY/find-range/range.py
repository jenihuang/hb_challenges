"""Given list of numbers, return smallest & largest number as a tuple.

For example::

    >>> find_range([3, 4, 2, 5, 10])
    (2, 10)

    >>> find_range([43, 3, 44, 20, 2, 1, 100])
    (1, 100)

For an empty list, it should return `None` as both smallest and largest::

    >>> find_range([])
    (None, None)

Make sure it works with a list of one item, which is both smallest and
largest::

    >>> find_range([7])
    (7, 7)
"""


def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple."""

    if not nums:
        return (None, None)
    elif len(nums) == 1:
        return (nums[0], nums[0])
    else:
        smallest = nums[0]
        largest = nums[0]
        for num in nums:
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num

    return(smallest, largest)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
