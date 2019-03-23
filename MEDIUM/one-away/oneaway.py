"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""
from collections import Counter


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""

    if len(w1) == len(w2):
        return change_letter(w1, w2)

    elif abs(len(w1) - len(w2)) == 1:
        return missing_letter(w1, w2)

    else:
        return False


# def missing_letter(w1, w2):
#     # create two dicts of letter counts, if there is one different valuesreturn True
#     a = Counter(w1)
#     b = Counter(w2)
#     diff_letter = False

#     for key in a.keys():
#         if key not in b:
#             if diff_letter:
#                 return False
#             else:
#                 diff_letter = True
#     return True

def missing_letter(w1, w2):

    inserted = False

    if len(w1) > len(w2):
        longer = w1
        shorter = w2
    else:
        longer = w2
        shorter = w1

    j = 0

    for i in range(len(longer)):
        if i == len(longer) - 1:
            return True
        elif longer[i] != shorter[j] and inserted:
            return False
        elif longer[i] != shorter[j]:
            inserted = True
            j = i
        else:
            j += 1

    return True


def change_letter(w1, w2):

    diff_letter = False

    for i in range(len(w1)):
        if w1[i] != w2[i]:
            if diff_letter:
                return False
            else:
                diff_letter = True

    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
