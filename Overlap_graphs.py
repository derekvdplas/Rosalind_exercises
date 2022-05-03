from collections import deque

with open(rosalind_grph.txt) as file:
  sample = file.read()

def clean_FASTA(sample):
    FASTA_lines = sample.split()
    complete_FASTA_lines = []
    DNA = ''
    for i in range(len(FASTA_lines)):
        if not FASTA_lines[i].startswith('>'):
            DNA += FASTA_lines[i]
        else:
            complete_FASTA_lines.append(DNA)
            header = FASTA_lines[i].replace('>', '')
            complete_FASTA_lines.append(header)
            DNA = ''

    complete_FASTA_lines = complete_FASTA_lines[1:]
    complete_FASTA_lines = complete_FASTA_lines[:40]
    paired_list = [[complete_FASTA_lines[i],complete_FASTA_lines[i+1]] for i in range(0,len(complete_FASTA_lines)-1,2)]
    return paired_list

def overlap_graph(seq):
    for i in range(len(seq)):
        d = deque(seq)
        d.rotate(-i)
        first, *rest = d

        for r in range(len(rest)):
            if first[1][-3:] == rest[r][1][:3]:
                print(first[0], rest[r][0])
    return

paired_list = clean_FASTA(sample)
overlap_graph(paired_list)
