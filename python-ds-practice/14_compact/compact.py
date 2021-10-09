def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    newlist = []
    for ele in lst:
        if ele:
            newlist.append(ele)
    return newlist
# Solution code:
#   return [val for val in lst if val]
