print("========== Bem Vindo(a) ao Menu de Jogos ==========")
print("Jogos:\n 1.Adivinhacao\n 2.FizzBuzz\n 3.Cara ou Coroa\n 4.JoKenPo\n")
jogo = input("Escolha qual jogo voce quer jogar: ").lower()
print()

if jogo == "1":
    import adivinhacao
elif jogo == "2":
    import FizzBuzz
elif jogo == "3":
    import cara_ou_coroa
else:
    import jokenpo