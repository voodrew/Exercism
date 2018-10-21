def product(numbers):
    total = 1
    for n in numbers:
        total *= n
    return total

def slice(sequence,length):
    return (sequence[i:i+length] for i in range(len(sequence) - length+1))

def largest_product(series, substring_length):
    if substring_length < 0:
        raise ValueError('substring length must be greater than zero')
    digits = [int(d) for d in series]
    return max(product(group) for group in slice(digits, substring_length))

