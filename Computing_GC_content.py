with open(rosalind_gc.txt) as file:
  FASTA = file.read()

FASTA_clean = FASTA.replace('\n', '')
separate_reads = FASTA_clean.split('>')


d = {}

for e in separate_reads:
    d[e[0:13]]=e[13::]
    
del d['']


highest_GC = 0
highest_GC_name = ''

for key, value in d.items():
    count = 0
    for i in value:
        if i == 'G' or i == 'C':
            count += 1
    
    GC = count / len(value)
    if GC > highest_GC:
        highest_GC = GC
        highest_GC_name = key
print(highest_GC_name + ' ' + str((highest_GC) * 100) + '%')

