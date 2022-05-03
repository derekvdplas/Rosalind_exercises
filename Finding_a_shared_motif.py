import numpy as np

with open(rosalind_revp) as file:
  FASTA = file.read()

def prep_fasta(FASTA):
    sequences = []
    lines = FASTA.splitlines()
    sequence = ''
    for line in lines:
        if line.startswith('>'):
            sequences.append(sequence)
            sequence = ''
        else:
            sequence += line.strip()
    if sequence != '':
        sequences.append(sequence)
    entries_removed = sequences[1:]
    return entries_removed

def common_substring(cleaned_fasta):
    longest_common_substring = ''
    # Have cut-off/slicing change with growing k-mer (starting from length 2), and ...
    for word_length in range(1,len(cleaned_fasta[0])):
        # Dividing into (growing) K-mers using word_length to stop making k-mers that are shorter then the ones we want to check this iteration
        for i in range(len(cleaned_fasta[0])-word_length):

            in_all = []
            # Check for all the k-mers if present in all entries
            for entry in cleaned_fasta:
                if cleaned_fasta[0][i:i+1+word_length] in entry:
                    in_all.append(True)
                else:
                    in_all.append(False)
            # Present in all entries?
            if all(in_all):        
                longest_common_substring = cleaned_fasta[0][i:i+1+word_length]


    return longest_common_substring



clean_fasta = prep_fasta(FASTA)
common_substring(clean_fasta)
