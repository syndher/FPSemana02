frase = input()
frase = frase.split(" ")
letras = frase.count("")
palavras_frase = {}

for palavra in frase:
    palavras_frase[palavra] = len(palavra)
print(palavras_frase)
