import sys

opcao = int(input("Escolha dentre as alternativas:\n [1]Verificar extrato \n [2]Saque"))
extrato = 500
limite = 300
if opcao == 1:
    print("Seu extrato é de R$500,00")
elif opcao == 2:
    sacar = float(input("Qual valor deseja sacar?"))
    if sacar <= extrato and sacar <= limite:
        print("Saque realizado")
    else:
        print("Saque indisponivel")

else: sys.exit("opçao invalida")