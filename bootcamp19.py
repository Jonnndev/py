print("-------------------")
print("Calculadora")
print("------------")
opcao = -1
while opcao != 0:
    opcao = int(input("Qual operacao deseja realizar? [1]Soma [2]Subtracao [3]Multiplicacao [4]Divisao"))
    if opcao == 1:
       num1 = float(input("Escolha um numero"))
       num2 = float(input("Escolha um numero"))
       soma = num1 + num2
       float(input(f"O resultado é {soma}"))
    if opcao == 2:
       num1 = float(input("Escolha um numero"))
       num2 = float(input("Escolha um numero"))
       subtracao = num1 - num2
       float(input(f"O resultado é {subtracao}"))
    if opcao == 3:
       num1 = float(input("Escolha um numero"))
       num2 = float(input("Escolha um numero"))
       multiplicacao = num1 * num2
       float(input(f"O resultado é {multiplicacao}"))
    if opcao == 4:
       num1 = float(input("Escolha um numero"))
       num2 = float(input("Escolha um numero"))
       divisao = num1 / num2
       float(input(f"O resultado é {divisao}"))