def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lower_letter = to_swap.lower()
    upper_or_lower = (lower_letter == to_swap)

    phrase.replace(if upper_or_lower =

    if letter is the same as toswap then replace it with "SWAPME"