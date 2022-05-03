n = 29
k = 4

babys_ls = 1
adults_ls = 0

for i in range(n-1):
  
    # Amount of adults in next year
    adults = adults_ls + babys_ls
    # Amount of babys in next year
    babys = adults_ls * k
    
    total = adults + babys

    adults_ls = adults
    babys_ls = babys

print(adults + babys)
