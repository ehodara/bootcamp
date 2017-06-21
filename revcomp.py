def complement_base(base, material='DNA'):
    """Returns the Watson-Crick complement of a base."""
    #Conver to lowercase
    base=base.lower()
    if base in 'Aa':
        if material=='DNA':
            return 'T'
        elif material=='RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'


def reverse_complement(seq, material='DNA'):
    """Compute reverse_complement of a sequence."""
    #Initialize the reverse complement
    rev_seq=' '
    for base in reversed(seq):
        rev_seq+= complement_base(base, material=material)

    return rev_seq
