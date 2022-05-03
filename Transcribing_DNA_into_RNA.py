with open('rosalind_rna.txt') as file:

   DNA_string = file.read()

def transcribe(DNA_string):
	RNA_string = DNA_string.replace('T','U')
	return RNA_string

transcribe(DNA_string)
