import numpy as np

# genotypes = [AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa]
test = '16372 17385 18100 18243 16486 19793'
replace_space = test.replace(' ',',')
list_of_string = replace_space.split(',')
list_of_couple_num = list(map(int, list_of_string))

chance_dominant_phenotype = [1, 1, 1, 0.75, 0.5, 0]

expected_values = np.multiply(list_of_couple_num, chance_dominant_phenotype)

# Two offspring per couple so multiply expected by 2
print(2 * sum(expected_values))
