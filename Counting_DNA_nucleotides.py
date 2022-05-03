with open('rosalind_dna.txt') as file:
   str = file.read()

count_A = 0
count_C = 0
count_G = 0
count_T = 0

for e in str:
	if e == 'A':
		count_A += 1
	if e == 'C':
		count_C += 1
	if e == 'G':
		count_G += 1
	if e == 'T':
		count_T += 1

print(count_A, count_C, count_G, count_T)
