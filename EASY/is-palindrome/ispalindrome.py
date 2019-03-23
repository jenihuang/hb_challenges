"""Is this word a palindrome?

    >>> is_palindrome("a")
    True

    >>> is_palindrome("noon")
    True

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("porcupine")
    False

Treat spaces and uppercase letters normally:

    >>> is_palindrome("Racecar")
    False
"""


def is_palindrome(word):
    """Return True/False if this word is a palindrome."""
    start = 0
    end = len(word) - 1

    while start <= end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1

    return True



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!")
