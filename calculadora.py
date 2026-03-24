numero = float(input("Digite um número: "))

while True:
    operacao = input("Digite +, -, * ou / (ou sair): ")

    if operacao == "sair":
        break

    outro = float(input("Digite outro número: "))

    if operacao == "+":
        numero = numero + outro
    elif operacao == "-":
        numero = numero - outro
    elif operacao == "*":
        numero = numero * outro
    elif operacao == "/":
        numero = numero / outro

    print("Resultado:", numero)
