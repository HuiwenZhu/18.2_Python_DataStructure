def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.

        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}

    If there are fewer values than keys, remaining keys should have value
    of None:

        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
# approach 1:
    new_dict = {}
    for index_key,key in enumerate(keys):
        new_dict[key]=values[index_key] if index_key<len(values) else None
# Another way using a feature from Python's standard library. We don't expect
    # you to have found this one---but it's a good example of how knowing the
    # standard library is so useful!

    # from itertools import zip_longest
    # return dict(zip_longest(keys, values))