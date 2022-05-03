k = 23 #homoz D
m = 28 #heteroz
n = 25 #homoz R

total = (k+m+n) -3

#If X is HH
HHpick = ((k-1) * 1 + m * 1 + n * 1) / ((k-1) + m + n)
print(str(HHpick) + ' is HHpick')

Hhpick = (k * 1 + (m-1) * 0.75 + n * 0.5) / (k + (m-1) + n)
print(str(Hhpick) + ' is Hhpick')

hhpick = (k * 1 + m * 0.5 ) / (k + m + (n-1))
print(str(hhpick) + ' is hhpick')

print((HHpick * k + Hhpick * m + hhpick * n) / (k+m+n))
