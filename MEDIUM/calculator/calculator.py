"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3

    >>> calc("- - 9 6 - 3 2") #(9 - 6) - (3 - 2)
    2
"""


def calc(s):
    """Evaluate expression."""

    items = s.split(' ')

    stack = []

    while items:
        current = items.pop()
        if current not in ['+', '-', '*', '/']:
            stack.append(current)
        else:
            n1 = int(stack.pop())
            n2 = int(stack.pop())
            if current == '+':
                result = n1 + n2
            elif current == '-':
                result = n1 - n2
            elif current == '*':
                result = n1 * n2
            else:
                result = int(n1 / n2)

            stack.append(result)

    return stack[0]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")
