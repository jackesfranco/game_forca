from palavraforca import palavras
import random

print("\n")
print("*" * 30)
print("\nSeja bem vindo ao jogo da forca!\n")
print("Neste jogo você deverá descobrir a palavra secreta!\n\nBoa sorte!\n")
print("*" * 30)
print("\n")

palavra = random.choice(palavras)
jogadas = []
chances = 7
ganhou = False

while True:

    for letra in palavra:
        if letra.lower() in jogadas:
            print(letra, end=" ")
        else:
            print("-", end=" ")
    print(f"\nVocê tem {chances} chances.")
    
    tentativa = input("\nEscolha uma letra para adivinhar: ")
    jogadas.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():
        chances -= 1
        print("Você errou, tente novamente!\n")

    ganhou = True
    for letra in palavra:
        if letra.lower() not in jogadas:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"\nParabéns, você ganhou! A palavra era: {palavra}.\n")

else:
    print(f"\nVocê perdeu! A palavra era: {palavra}.\n")
