"""Parse an unbroken sentence into possible words.

Example:

    >>> sentences = parse('iatenoodlesfordinnertonight', vocab)

    >>> for s in sorted(sentences):
    ...    print(s)
    i a ten oodles for dinner to night
    i a ten oodles for dinner tonight
    i a ten oodles ford inner to night
    i a ten oodles ford inner tonight
    i ate noodles for dinner to night
    i ate noodles for dinner tonight
    i ate noodles ford inner to night
    i ate noodles ford inner tonight

"""

vocab = {'i', 'a', 'ten', 'oodles', 'ford', 'inner', 'to', 'night',
         'ate', 'noodles', 'for', 'dinner', 'tonight'}


def parse(phrase, vocab):
    """Break a string into words.

    Input:
        - string of words without space breaks
        - vocabulary (set of allowed words)

    Output:
        set of all possible ways to break this down, given a vocab
    """


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB! ***\n")

