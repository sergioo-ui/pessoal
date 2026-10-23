import random

num = random.randint(1, 50)
tentativas = 5

while tentativas > 0:
    chute = int(input("Digite um numero entre 1 e 50: "))
    if chute == num:
        print("Voce acertou!")
        break
    elif chute > num:
        print("Menor!")
    else:
        print("Maior!")
    tentativas -= 1
    
if tentativas == 0:
    print("Voce perdeu!")
    print(f"O numero era {num}")