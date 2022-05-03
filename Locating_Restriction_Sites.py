with open(rosalind_revp.txt) as file:
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

def reverse_palindrome(line):
    line = line[0]
    nucleo_complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    for kmer_length in range(4,13,2):
        # For all k-mer 4 to 12, dont bother with unevens because there are no uneven k-mer reverse palindromes possible
        # Go over all possible kmers, and stop on time with minus kmer_length
        for i in range(len(line)-kmer_length+1):
            kmer = line[i:i+kmer_length]
            is_reverse_palindrome_nucl = []
            for n in range(int((len(kmer))/2)):
                # Check if reverse palindrome for first half of kmer,
                # to also check second half would be double work since comparing first and complement of last element of k-mer, is the same as comparing last and complement of first
                if kmer[n] == nucleo_complement.get(kmer[-(n+1)]):
                    is_reverse_palindrome_nucl.append(True)
                else:
                    is_reverse_palindrome_nucl.append(False)
            if all(is_reverse_palindrome_nucl):
                print(i+1, kmer_length)
    return

entries_rem = prep_fasta(FASTA)
reverse_palindrome(entries_rem)

#    return position, length
