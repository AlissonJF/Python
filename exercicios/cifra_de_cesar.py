modo_escript = 1
modo_descript = 0

def cesar(data, chave, modo):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    new_data = ''
    new_index = 0
    for c in data:
        index = alfabeto.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = new_index % len(alfabeto)
            if modo == modo_escript:
                new_index = index + chave
            elif modo == modo_descript:
                new_index = abs (chave - index-chave)
           
            new_data += alfabeto[new_index]

    return new_data

chave = int(input('Digite o valor da chave: '))
frase = 'este eh um teste'
print('Frase: ',frase)
criptografia = cesar(frase, chave, modo_escript)
print('Criptografia: ',criptografia)
descriptografia = cesar(frase, chave, modo_descript)
print('Descriptografia: ', descriptografia)