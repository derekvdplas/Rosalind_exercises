RNA_codon_table = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
                   "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
                   "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
                   "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
                   "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
                   "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
                   "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
                   "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
                   "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
                   "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
                   "UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E",
                   "UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
                   "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
                   "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
                   "UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G",
                   "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"}

def rna_to_prot(rna_seq):
    prot_seq = ''
    tri_nucl = [rna_seq[i:i + 3] for i in range(0, len(rna_seq), 3)]
    for n in tri_nucl:
        amino = RNA_codon_table.get(n)
        if amino == "Stop":
            break
        prot_seq += amino
    print(prot_seq)
    return prot_seq
  
with open(rosalind_prot.txt) as file:
  RNA_string = file.read()

rna_to_prot(RNA_string)
