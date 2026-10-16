print("========== Bem Vindo(a) a Calculadora em Python ==========")

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))
op = input("Operacoes: \n 1.Adicao\n 2.Subtracao\n 3.Multiplicacao\n 4.Divisao\n Escolha a operacao: ")

if op == "1":
    print(f"{n1} + {n2} =", n1 + n2)
elif op == "2":
    print(f"{n1} - {n2} =", n1 - n2)
elif op == "3":
    print(f"{n1} * {n2} =", n1 * n2)
elif op == "4":
    if n2 == 0:
        print("Nao eh possivel dividir por zero!")
    print(f"{n1} / {n2} =", n1 / n2)
else:
    print("Entrada invalida!")    
