"""Find the largest of three numbers.

Define a function max_of_three() that takes in three numbers as arguments and
returns the largest of them. Do not use the built in 'max' method.

For example::

    >>> max_of_three(1, 3, 2)
    3

    >>> max_of_three(5, 5, 5)
    5

    >>> max_of_three(10, 2, 11)
    11

    >>> max_of_three(5, 5, 10)
    10

"""


def max_of_three(num1, num2, num3):
    """Returns the largest of three integers"""

    m = num1
    if num2 > m:
        m = num2

    if num3 > m:
        m = num3

    return m


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. MAXIMALLY EXCELLENT!\n")
