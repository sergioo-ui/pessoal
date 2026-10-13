import random

moeda = ["cara", "coroa"]
escolha = input("Escolha entre cara ou coroa: ").lower()
resultado = random.choice(moeda)
print(f"Saiu {resultado}.")
if escolha == resultado:
    print("Voce venceu!")
else:
    print("Voce perdeu!")