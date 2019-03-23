"""Find the subsequence with the largest sum.

Given a list of integers, like:

  [1, 0, 3, -8, 4, -2, 3]

Return the contiguous subsequence with the largest sum. For
that example, the answer would be [4, -2, 3], which sums to 5.


    >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    [19]

For ties, return the first one:

    >>> largest_sum([2, 2, -10, 1, 3, -20])
    [2, 2]

Return the shortest version:

    >>> largest_sum([2, -2, 3, -1])
    [3]

If the list is all negative numbers, the subsequence
with the highest sum will be empty (ie, we can do no better
than pick nothing!):

    >>> largest_sum([-1, -2])
    []
"""


# def largest_sum(nums):
#     """recursive call each array and break off beginning and end
#     get sum of current, replace out array if needed"""

#     return largest_sum_helper(nums, [])


# def largest_sum_helper(nums, output):

#     if not nums:
#         return output
#     if sum(nums) < 0:
#         return []
#     else:
#         current_sum = sum(nums)
#         output_sum = sum(output)
#         if current_sum > output_sum:
#             left = largest_sum_helper(nums[1:], nums)
#             right = largest_sum_helper(nums[:-1], nums)
#             if sum(left) > sum(right):
#                 return left
#             else:
#                 return right
#         else:
#             left = largest_sum_helper(nums[1:], output)
#             right = largest_sum_helper(nums[:-1], output)
#             if sum(left) > sum(right):
#                 return left
#             else:
#                 return right


def largest_sum(nums):
    """Find subsequence with largest sum."""
    max_nums = []
    added_nums = []

    for num in nums:
        added_nums.append(num)
        if sum(added_nums) <= 0:
            added_nums = []
        if sum(added_nums) > sum(max_nums):
            max_nums = added_nums[:]

    return max_nums


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU HANDLED THIS SUMMARILY!\n")
