import random
import time
from colorama import Fore
from colorama import Style
from colorama import Back

nome = input(f'{Fore.YELLOW}---------------------------------Qual seu nome Herói?---------------------------------\n{Style.RESET_ALL}')

pacote = ["goblin", "Demonyc Eye", "Zombie"]

monstro_escolhido = random.choice(pacote)

ErrouAtaque = 0

print(' ')
print(f'{Fore.MAGENTA}Oh, um {monstro_escolhido} apareceu ;-;{Style.RESET_ALL}')
print(' ')

jogador = 100
monstro = 100

#Seu ataque

while jogador > 1:
    time.sleep(1)
    print('---------------------------------')
    print(' ')
    print(f'{nome} Seu nível de HP é de {jogador}\nO nível de HP do {monstro_escolhido} é {monstro}')
    print(' ')
    time.sleep(1)
    print(f'O que vai fazer {nome}!?')
    
    ataque = int(input(f'{Fore.RED}Opção 1: ataque fraco\n{Fore.GREEN}Opção 2: ataque forte\n{Fore.BLUE}Opção 3: recuperar HP\n{Style.RESET_ALL}'))
    print(' ')

    if ataque == 1:
        time.sleep(1)
        monstro -= 15
        print(f'{monstro_escolhido} sofreu 15 de dano!')
        print(f'{monstro_escolhido} está com {monstro} de HP')
    
    elif ataque == 2:
        time.sleep(1)
        chance = random.randint(1,2)
        if chance == 1:
            monstro -= 25
            print(f'{monstro_escolhido} sofreu 25 de dano!')
            print(f'{monstro_escolhido} está com {monstro} de HP!')
        
        elif chance == 2:
            time.sleep(1)
            print('Você errou seu ataque!')
            ErrouAtaque += 1

            if ErrouAtaque >= 3:
                jogador += 5
                print(" ")
                time.sleep(1)
                print("Você é Decepcionante... toma 5 de HP KKKK")
                ErrouAtaque = 0

    elif ataque == 3:
        time.sleep(1)
        jogador += 15
        print('Você recuperou 15 de HP!')
        time.sleep(1)
        print(f'Você está com {jogador} de HP')

    else:
        print('Digito incorreto! favor digitar apenas as opções dadas acima :/')
        continue
    
# Ganhar ou Perder 1

    if monstro < 1:
        time.sleep(1)
        print('Você ganhou essa partida \o/')
        print('O monstro finalmente morreu!!')
        break

    elif jogador < 1:
        time.sleep(1)
        print('Você perdeu essa partida :/')
        print(' ')
        recomecar = (input('Gostaria de tentar novamente?\nSim para continuar\nNao para finalizar\n'.upper()))

        if recomecar == 'SIM':
            jogador = 100
            monstro = 100
            continue
        elif recomecar == 'NAO' or recomecar == 'NÃO':
            break

# Ataque Inimigo
    print('===========================')
    print(' ')
    print(f'O {monstro_escolhido} vai atacar!')
    time.sleep(2)
    print(' ')

    ataque_inimigo = random.randint(1,3)

    if ataque_inimigo == 1:
        time.sleep(1)
        jogador -= 15
        print(f'Você sofreu 15 de dano!')
        
    elif ataque_inimigo == 2:
        time.sleep(1)
        jogador -= 20
        print('Você sofreu 20 de dano')

    elif ataque_inimigo == 3:
        time.sleep(1)
        monstro += 10
        print(f'O {monstro_escolhido} recuperou 10 de dano ºoº')

# Ganhar ou Perder 2

    if monstro < 1:
        time.sleep(1)
        print('Você ganhou essa partida \o/')
        print('O monstro finalmente morreu!!')
        break

    elif jogador < 1:
        time.sleep(1)
        print('Você perdeu essa partida :/')
        print(' ')
        break