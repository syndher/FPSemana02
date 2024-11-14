frase = input()
frase = frase.split(" ")
letras = frase.count("")
palavras_frase = {}

for palavra in frase:
    b = len(palavra)
    palavras_frase[str(palavra), b]
print(palavras_frase)
