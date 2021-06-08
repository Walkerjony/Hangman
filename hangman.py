import random
from time import *

lista = ('Batata', 'Computador', 'Cidade', 'Mesa')
palavra = random.choice(lista)
letters_guessed = len(palavra) * "_"
erro = 0
wrd = ''
chances = 6
nome = input("Digite seu nome: ")
print("*===============================*")
print("A palavra possui ", len(letters_guessed), "Letras")
print("*===============================*")

while chances > 0:
        erro = 0
        for i in palavra:
            if i in wrd:
                print(i)
            else:
                print("_")
                erro += 1
        if erro == 0:
            print(f'Parabéns {nome}, Você ganhou!!')
            sleep(3)
            break
        letra = input("Digite uma letra: ")
        wrd = wrd + letra

        if letra not in palavra:
            chances -= 1
            print("Letra errada!")
            print(f'Voce ainda tem {chances} tentativas!')
        if chances == 0:
            print(f"Não foi dessa vez.. A palavra correta era: {palavra}")

