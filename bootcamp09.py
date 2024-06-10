import sys

opcao = float(input("Escolha quais das funçoes voce quer utilizar \n [1] Sacar \n [2] Verificar o Extrato \n"))
extrato = 250

if opcao == 1:
    saque = float(input("Qual valor o senhor(a) deseja sacar?"))
    if saque <= extrato:
        print("Saque realizado")
    else:
        print("Saldo insuficiente")

elif opcao == 2:
    print("Valor do seu extrato é",extrato)

else:
    sys.exit("Opçao invalida")