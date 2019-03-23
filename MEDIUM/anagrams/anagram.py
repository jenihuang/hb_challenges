"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:
    >>> import os, sys
    >>> all_words = [w.strip() for w in open(os.path.join(sys.path[0],'words.txt'))]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""
from collections import Counter, defaultdict


# def find_most_anagrams_from_wordlist(wordlist):
#     """Given list of words, return the word with the most anagrams."""
#     all_words_dict = {}
#     most = {'word': wordlist[0], 'anagrams': 1}

#     for word in wordlist:
#         count = Counter(word)
#         f = frozenset(count)
#         if f not in all_words_dict:
#             all_words_dict[f] = [word, 1]
#         else:
#             all_words_dict[f][1] += 1
#             if all_words_dict[f][1] > most['anagrams']:
#                 most['word'] = all_words_dict[f][0]
#                 most['anagrams'] = all_words_dict[f][1]

#     return most['word']

def make_anagram_dict(words):
    """Return dict mapping sorted letters -> [words w/ those letters]

        >>> (make_anagram_dict(["act", "cat", "dog", "god"]) ==
        ... {'dgo': ['dog', 'god'], 'act': ['act', 'cat']})
        True
    """
    out = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(list(word)))
        out[sorted_word].append(word)

    return out


def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""

    all_words_dict = make_anagram_dict(wordlist)
    most_count = 0
    most_word = None

    for value in all_words_dict.values():
        if len(value) > most_count:
            most_count = len(value)
            most_word = value[0]

    return most_word


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
