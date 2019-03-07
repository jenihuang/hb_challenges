def recursive_index_helper(word, lst, index):

    if len(lst) == 0:
        return None
    elif word == lst[0]:
        return index
    else:
        return recursive_index_helper(word, lst[1:], index + 1)


def recursive_index(word, lst):

    return recursive_index_helper(word, lst, 0)


print(recursive_index('train', ['hey', 'there',
                                'you', 'welcome', 'to', 'the', 'train']))
