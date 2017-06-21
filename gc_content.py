seq='GACAGACUCCAUGCACGUGGGUAUCUGUC'

#Initialize the GC counter
n_gc=0

#Initialize sequence length
len_seq=0

#Loop through sequence and count G's and C's
for base in seq:
    len_seq+=1
    if base in 'GCgc':
        n_gc+=1

#Divide to get GC content
n_gc/len_seq

print(n_gc/len(seq))
