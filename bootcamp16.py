import sys

opcao = -1

while opcao != 0:
    opcao = int(input("[1]Sacar \n[2]Extrato \n[0]Sair \n"))
    if opcao == 1:
        print("Realizando o saque")
    elif opcao == 2:
        print("Verificando o extrato")
else:
    sys.exit(print("Desculpe, mas o sistema nao tem alternativas"))