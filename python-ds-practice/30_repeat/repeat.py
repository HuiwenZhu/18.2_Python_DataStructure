def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    if isinstance(num, int) and num > 0:
        new_str = ''
        for i in range(num):
            new_str = new_str+phrase
        return new_str
    if num == 0:
        return ''
    return None

    # if not isinstance(num, int) or num < 0:
    #     return None

    # return phrase * num
