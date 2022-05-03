import numpy as np
import pandas as pd

'''
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

OUTPUT
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
CONSENSUS
'''


# 1. filter file and put in array
# 2. count array values on indices
# 3. make consensus

with open(rosalind_cons.txt) as file:
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
    entries_removed = sequences[1:]
    DNA_array = np.array(entries_removed)
    return DNA_array


def counting_values(_array):
    consensus_nucl_dict = {}
    A = np.zeros(len(_array[0]), dtype=int)
    G = np.zeros(len(_array[0]), dtype=int)
    T = np.zeros(len(_array[0]), dtype=int)
    C = np.zeros(len(_array[0]), dtype=int)
    
    for i in range(len(_array[0])):
        # Go over all first, second, third... letter in each string
        for j in range(len(_array)):
            if _array[j][i] == 'A':
                A[i] += 1
            if _array[j][i] == 'G':
                G[i] += 1
            if _array[j][i] == 'T':
                T[i] += 1
            if _array[j][i] == 'C':
                C[i] += 1
    consensus_nucl_dict["A"] = A
    consensus_nucl_dict["G"] = G
    consensus_nucl_dict["T"] = T
    consensus_nucl_dict["C"] = C
    return(consensus_nucl_dict)

def consensus(consensus_nucl_dict):
    key_list = list(consensus_nucl_dict.keys())
    val_list = list(consensus_nucl_dict.values())

    consensus_seq = ''
    position_matrix = pd.DataFrame(columns=['A','G','T','C'])

    for i in range(len(list(consensus_nucl_dict.values())[0])):
        position = []
        # For every nucleotide count in every 'word' ...
        for j in range(len(list(consensus_nucl_dict.values()))):
            position.append(list(consensus_nucl_dict.values())[j][i])
        position_matrix.loc[len(position_matrix.index)] = position
        highest_in_position = max(position)

        # 0 = A, 1= G, 2= T, 3 = C
        nucl_pos = position.index(highest_in_position)
        if nucl_pos == 0:
            consensus_seq += 'A'
        if nucl_pos == 1:
            consensus_seq += 'G'
        if nucl_pos == 2:
            consensus_seq += 'T'
        if nucl_pos == 3:
            consensus_seq += 'C'
    position_matrix = position_matrix.T
    return consensus_seq, position_matrix


DNA_array = prep_fasta(FASTA)
consensus_nucl_dict = counting_values(DNA_array)
consensus(consensus_nucl_dict)
