palavra1 = input()
palavra2 = input()
set1 = {}
set2 = {}
for letra in palavra1:
    set1.update([letra])

for letra in palavra2:
    if letra in set1:
        set2.update([letra])

   
print(palavra1)
print(palavra2)
print(set2)