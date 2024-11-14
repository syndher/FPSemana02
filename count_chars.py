frase = input()
frase = frase.split(" ")
palavras_frase = {}

for palavra in frase:
    palavras_frase[palavra] = len(palavra)
print(palavras_frase)
