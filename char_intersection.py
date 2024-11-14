palavra1 = input()
palavra2 = input()
conjunto = ""
for letra in palavra1:
    set(palavra1)

for letra in palavra2:
    if letra in palavra1:
        if letra not in conjunto:
            conjunto += letra
        
print(palavra1)
print(palavra2)
print(conjunto)