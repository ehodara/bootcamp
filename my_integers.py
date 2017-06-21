my_integers=['ignition',1,2,3,4,5,6,7,8,9,10]

for n in reversed(my_integers):
    print(n)

start_codon='AUG'
seq='GUAGUAUAUAGCAUAUUAUCUAAUGCUAGUCGACAUCCCACG'
#Initialize sequence index
i=0
#Scan the sequence until start codon
while seq[i:i+3] !=start_codon and i<len(seq):
    i+=1

if i==len(seq):
    print('Start codon not found.')
else:
    print('Start codon at index',i)
