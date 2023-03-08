lista = []

def carrinho ():
    item = ''

    while True:
        item = input("Digite o item que será inserido no carrinho: ")
        if (item == 'sair'):
            print('')
            print(lista)
            break
        lista.append(item)

def menu():
    while True:
        print('')
        print('Gostaria de adicionar algum item?\n')
        print('')
        item = input('Sim -> S\nMostrar Lista de itens -> listar\nRemover Item -> R\nFechar Programa -> Pressione a tecla Ctrl + C\n\nDigite aqui: ')
        print('')
        if (item == 'S'):
            for i in range (len (lista)):
                print("Digite o valor: %s | Para remover o item: %s" % (i,lista[i]))
            print('')
            carrinho()
            menu()
        elif (item == 'R'):
            removeItem()
            menu()
        elif (item == 'listar'):
            for i in range(len (lista)):
                print('Item: %s' % (lista[i]))
        else:
            break
        

def removeItem():
    while True:
        for i in range(len (lista)):
            print('Digite o valor: %s | Para remover o item: %s' % (i,lista[i]))
        print('')
        item = input('Insira um item citado acima para removê-lo da lista: ')
        if (item == 'sair'):
            print(lista)
            break
        lista.pop(int(item))
        print('')


menu()