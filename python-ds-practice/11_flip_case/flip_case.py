def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # lower=to_swap.lower()
    # flipped=""
    # for char in phrase:
    #     if char.lower()==lower:
    #         char=char.swapcase()
    #     flipped+=char

    # return flipped




# ALTERNATIVE:
    to_swap = to_swap.lower()
        
    fixed = [
        (char.swapcase() if char.lower() == to_swap else char)
         for char in phrase
    ]
        
    return "".join(fixed)