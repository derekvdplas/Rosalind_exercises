nucleo_pair = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

with open(rosalind_revc.txt) as file:
    DNA_string = file.read()

def reverse_compl(DNA_string):
    compl_DNA_string = ''
    for nucleotide in DNA_string:
        compl_DNA_string += nucleo_pair[nucleotide] 
    compl_DNA_string_reversed = compl_DNA_string[::-1]
    return compl_DNA_string_reversed
  
  reverse_compl(DNA_string)
