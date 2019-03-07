"""Simple infix calculator.

    >>> calc("1 + 2")
    3

    >>> calc("2 * 3")
    6

    >>> calc("2 * ( 1 + 2 )")
    6

    >>> calc("( 2 * 1 ) + 2")
    4

    >>> calc("( ( 1 + 2 ) * ( 3 + 4 ) ) - ( 2 * ( 1 + 3 ) )")
    13
"""


def calc(s):
    """Simple infix calculator."""

