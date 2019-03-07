"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8

    """
    # all_nums = set()

    # for i in range(1, max_num + 1):
    #     all_nums.add(i)

    # for num in nums:
    #     if num not in all_nums:
    #         return num

    sum_n = (max_num * (max_num + 1)) / 2

    total = 0
    for item in nums:
        total += item

    return int(sum_n - total)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
