"""Find segments comprising >2 points.

Given a list of points in a 2d space, find segments that use 3+ of those
points. Return this as a list of segments, where each segment is a list
of the component points. (For clarity, sort the output).

There are no 3+ segments here::

    >>> _(sameline([(0, 0), (1,1), (3,2), (4,3)]))
    []

There are two 3+ segments here::

    >>> _(sameline([(0,0), (1,1), (2,3), (3,2), (3,3), (3,4)]))
    [[(0, 0), (1, 1), (3, 3)], [(3, 2), (3, 3), (3, 4)]]

These are the same input point, in a different order --- the output should
be exactly the same, though.

    >>> _(sameline([(3,4), (3,3), (3,2), (2,3), (1,1), (0,0)]))
    [[(0, 0), (1, 1), (3, 3)], [(3, 2), (3, 3), (3, 4)]]

Other examples::

    >>> _(sameline([(0,0), (3,4)]))
    []

    >>> _(sameline([(0,0), (2,1), (2,0), (4,2), (2,2)]))
    [[(0, 0), (2, 1), (4, 2)], [(2, 0), (2, 1), (2, 2)]]

    >>> _(sameline([(0., 0.), (1., 1.), (3., 4.), (2., 2.)]))
    [[(0.0, 0.0), (1.0, 1.0), (2.0, 2.0)]]

    >>> _(sameline([(0,0), (3,4), (7, 21)]))
    []
"""

from collections import defaultdict
import itertools


def sameline(pts):
    """Find segments comprising >2 points."""

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE NOT OUT OF LINE!\n")
