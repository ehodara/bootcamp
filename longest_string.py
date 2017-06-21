seq1='AATCTACTAGT'
seq2='CATCGCTATCT'

def longest_common_substring(seq1,seq2):
    def num_substrings(seq1,i):
        return((len(seq1)-i)+1)

        for i in reversed(range(len(seq1)+1)):

            for j in range(num_substrings(len(seq1), i)):
                seq1[j:j+i]
                if seq1[j:j+i] in seq2:
                    return (seq1[j:j+i])

print (longest_common_substring(seq1,seq2))
