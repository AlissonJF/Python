frase = input('Digite a frase: ').split()

tam_palavra = list()

for palavra in frase:
    tam_palavra.append(len(palavra))

maior = max(tam_palavra)
print('Maior palavra: ')
for a, b in zip(frase ,tam_palavra):
    if b == maior:
        print(a)