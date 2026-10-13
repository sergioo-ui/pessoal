import random

itens = ["pedra", "papel", "tesoura"]
player = input("Escolha entre pedra, papel ou tesoura: ").lower()
COM = random.choice(itens)
print(f"Voce escolheu: {player}")
print(f"O computador escolheu: {COM}")
if player == COM:
    print("Empate!")
elif player == "pedra" and COM == "tesoura":
    print("Voce venceu!")
elif player == "papel" and COM == "pedra":
    print("Voce venceu!")
elif player == "tesoura" and COM == "papel":
    print("Voce venceu!")
else:
    print("O computador venceu")