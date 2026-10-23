print("========== Bem Vindo(a) ao Menu de Jogos ==========")
print("Jogos:\n 1.Adivinhacao\n 2.FizzBuzz\n 3.Cara ou Coroa\n 4.JoKenPo\n 5.Jogo da Velha\n")
jogo = input("Escolha qual jogo voce quer jogar: ").lower()
print()

if jogo == "1":
    import adivinhacao
elif jogo == "2":
    import FizzBuzz
elif jogo == "3":
    import cara_ou_coroa
elif jogo == "4":
    import jokenpo
elif jogo == "5":
    import jogo_da_velha
    jogo_da_velha.jogar()
else:
    print("Opção inválida.")