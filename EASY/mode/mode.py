"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""

from collections import defaultdict

def mode(nums):
    """Find the most frequent num(s) in nums."""

    c = defaultdict(int)
    
    for num in nums:
        c[num] += 1

    highest = max(c.values())

    s = set()

    for num, count in c.items():
        if count == highest:
            s.add(num)

    return s



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
