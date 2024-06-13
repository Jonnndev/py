print("-------------------")
print("Calculadora")
print("------------")

opcao = -1

while opcao != 0:
    opcao = int(input("Qual operacao deseja realizar? [1]Soma [2]Subtracao [3]Multiplicacao [4]Divisao [0]Sair"))
    if opcao == 1:
        num1 = float(input("Informe um numero"))
        num2 = float(input("Informe outro numero"))
        soma = num1 + num2
        print(f"O Resultado da soma foi de {soma}")
    if opcao == 2:
        num1 = float(input("Informe um numero"))
        num2 = float(input("Informe outro numero"))
        sub = num1-num2
        print(f"O resultado da subtracao foi de {sub}")