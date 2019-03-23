"""Count words in a sentence, and print in ascending order.

For example::

    >>> word_count("berry cherry cherry cherry berry apple")
    apple: 1
    berry: 2
    cherry: 3

If there is a tie for a count, make sure the words are printed in
ascending order within the tie::

    >>> word_count("hey hi hello")
    hello: 1
    hey: 1
    hi: 1

Capitalized words are considered distinct::

    >>> word_count("hi Hi hi")
    Hi: 1
    hi: 2
"""

from collections import Counter

def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""

    words = phrase.split(' ')
    word_counts = Counter(words)
    counts = [(count, word) for word,count in word_counts.items()]
    counts.sort()
    for item in counts:
        print('{}: {}'.format(item[1],item[0]))


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
