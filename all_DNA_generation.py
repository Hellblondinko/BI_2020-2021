import itertools


nucleotides = ['A', 'T', 'G', 'C']
def random_dna_sequence(length):
    for i in range(1, length+1):
        combinations = itertools.product(*itertools.repeat(nucleotides, i))
        for j in combinations:
            yield (''.join(j))




