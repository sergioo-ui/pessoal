peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)
print(f"IMC: {imc:.1f}")

if imc < 18.5:
    print("Subpeso.")
elif imc < 25:
    print("Normal.")
elif imc < 30:
    print("Sobrepeso.")
elif imc < 35:
    print("Obesidade Grau 1.")
elif imc < 40:
    print("Obesidade Grau 2.")
else:
    print("Obesidade Morbida.")