seq='GATCTAGCTGATCGAGCGCAAATGCTAATCTACTGGGCAGCAT'
#Initialize the reverse complement
def reverse_complement(seq):
    seq=seq[::-1].replace('G','c')
    seq=seq.replace('C','G')
    seq=seq.replace('T','a')
    seq=seq.replace('A','T')
    seq=seq.upper()
    return seq

print(reverse_complement(seq))
