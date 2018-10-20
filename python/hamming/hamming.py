def distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("Strands are not the same length!")

    return sum(1 for a,b in zip(dna1, dna2) if a != b)