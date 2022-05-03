with open(rosalind_orf.txt) as file:
  dataset = file.read()
  
  
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

nucleo_complement = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}


def clean_up(dataset, remove_header = False):
    dataset_mRNA = dataset.replace('T','U')
    FASTA_lines = dataset_mRNA.split()
    complete_FASTA_lines = []
    DNA = ''
    for i in range(len(FASTA_lines)):
        if not FASTA_lines[i].startswith('>'):
            DNA += FASTA_lines[i]
        else:
            complete_FASTA_lines.append(DNA)
            header = FASTA_lines[i].replace('>', '')
            if remove_header is False:
                complete_FASTA_lines.append(header)
            DNA = ''
    if DNA != '':
        complete_FASTA_lines.append(DNA)
    complete_FASTA_lines_no_entry = complete_FASTA_lines[1:]
    return complete_FASTA_lines_no_entry

def dna_to_prot(dna_seq):
    # Check 3 leading frames
    dna_seq = dna_seq[0]
    for k in range(2):
        for j in range(3):
            prot_seq = ''
            for i in range(j, len(dna_seq)-3+j, 3):
                tri_nucl = dna_seq[i:i + 3]
                amino = RNA_codon_table.get(tri_nucl)
                if amino == "Stop":
                    break
                prot_seq += amino
            print(prot_seq)

        dna_seq_reverse = dna_seq[::-1]
        reverse = ''
        for b in dna_seq_reverse:
            reverse += nucleo_complement.get(b)
        dna_seq = reverse
    return 0


dataset = clean_up(dataset,remove_header = True)
dna_to_prot(dataset)
