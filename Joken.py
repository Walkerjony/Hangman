from random import randint

lista = ("Pedra", "Papel", "Tesoura")
count = 0
count1 = 0
i = 0

nome = str(input("Digite seu nome"))
escolha = str(input("y para melhor de 3 ou x para melhor de 5"))

if escolha == 'y':
    while i < 3:

        jogador = int(input('''Escolha uma opcao para se jogar: 

    [0] Pedra
    [1] Papel
    [2] Tesoura

    Digite sua escolha: '''))
        computador = randint(0, 2)

        print(f'O jogador escolheu ---> {lista[jogador]}')
        print(f'O computador escolheu -----> {lista[computador]}')

        if computador == 0:
            if jogador == 0:
                i += 1
                print(f'Placar: {count} X {count1}')
            elif jogador == 1:
                i += 1
                count += 1
                print(f'Placar: {count} X {count1}')
            elif jogador == 2:
                i += 1
                count1 += 1
                print(f'Placar: {count} X {count1}')


        elif computador == 1:
            if jogador == 0:
                i += 1
                count1 += 1
                print(f'Placar: {count} X {count1}')
            elif jogador == 1:
                i += 1
                print(f'Placar: {count} X {count1}')
            elif jogador == 2:
                i += 1
                count += 1
                print(f'Placar: {count} X {count1}')


        elif computador == 2:
            if jogador == 0:
                i += 1
                count += 1
                print(f'Placar: {count} X {count1}')
            elif jogador == 1:
                i += 1
                count += 1
                print(f'Placar: {count} X {count1}')
            elif jogador == 2:
                i += 1
                print(f'Placar: {count} X {count1}')

if count > count1:
    print(f'{nome} venceu a partida!')
if count1 > count:
    print("Computador venceu a partida!")

if escolha == 'x':

    while i < 5:

        jogador = int(input('''Escolha uma opcao para se jogar: 

    [0] Pedra
    [1] Papel
    [2] Tesoura

    Digite sua escolha: '''))
        computador = randint(0, 2)

        print(f'O jogador escolheu ---> {lista[jogador]}')
        print(f'O computador escolheu -----> {lista[computador]}')

        if computador == 0:
            if jogador == 0:
                i += 1
                print(f'Placar: {count} X {count1}')
            elif jogador == 1:
                i += 1
                count += 1
                print(f'Placar: {count} X {count1}')
            elif jogador == 2:
                i += 1
                count1 += 1
                print(f'Placar: {count} X {count1}')


        elif computador == 1:
            if jogador == 0:
                i += 1
                count1 += 1
                print(f'Placar: {count} X {count1}')
            elif jogador == 1:
                i += 1
                print(f'Placar: {count} X {count1}')
            elif jogador == 2:
                i += 1
                count += 1
                print(f'Placar: {count} X {count1}')


        elif computador == 2:
            if jogador == 0:
                i += 1
                count += 1
                print(f'Placar: {count} X {count1}')
            elif jogador == 1:
                i += 1
                count += 1
                print(f'Placar: {count} X {count1}')
            elif jogador == 2:
                i += 1
                print(f'Placar: {count} X {count1}')

if count > count1:
    print(f'{nome} venceu a partida!')
if count1 > count:
    print("Computador venceu a partida!")