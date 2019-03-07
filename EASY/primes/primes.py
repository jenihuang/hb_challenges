"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""

import math


def is_prime(num):
    """Is a number a prime number?"""

    if num < 2:
        return False

    sr = int(math.sqrt(num))

    for i in range(2, sr + 1):

        if num % i == 0:
            return False

    return True


def primes(count):
    """Return count number of prime numbers, starting at 2."""
    # while primes_count is less than count, check all numbers starting from 2 if prime add to list

    primes_count = 0
    results = []
    i = 2

    while primes_count < count:

        if is_prime(i):
            results.append(i)
            primes_count += 1

        i += 1

    return results


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
