def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    newlist = list(phrase.lower().replace(' ', ''))
    reversed_list =newlist[::-1]
    if reversed_list==newlist:
        return True
    else:
        return False
#  solution code
        # normalized = phrase.lower().replace(' ', '')
        # return normalized == normalized[::-1]
