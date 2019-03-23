"""Return longest word in list of words.

For example::

    >>> find_longest_word(["hi", "hello"])
    5

    >>> find_longest_word(["Balloonicorn", "Hackbright"])
    12

"""


def find_longest_word(words):
    """Return longest word in list of words."""

    longest = words[0]
    count = len(words[0])

    for word in words:
        if len(word) > count:
            count = len(word)
            longest = word

    return count


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE THE MAX!\n")
