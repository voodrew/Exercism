def on_square(sq):
    if sq > 64:
        raise ValueError('too many squares')
    if sq < 1:
        raise ValueError('only non-negative squares')
    return 2**(sq-1)


def total_after(sq):
    if sq > 64:
        raise ValueError('too many squares')
    if sq < 1:
        raise ValueError('only non-negative squares')
    return sum(2**(i-1) for i in range(1, sq+1))
