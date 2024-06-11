import sys

conta_normal = 1
conta_universitaria = 2
saldo = 500
cheque_especial = 500
escolha_conta = float(input("Sua conta é [1]Universitaria ou [2]Normal"))


if escolha_conta == 2:
    saque = float(input("Qual valor deseja sacar?"))
    if saque <= saldo + cheque_especial:
        print("Saque efetuado")
    else:
        print("Nao é possivel efetivar o saque")
elif escolha_conta == 1:
    saque = float(input("Qual valor deseja sacar?"))
    if saque <= saldo:
        print("Saque efetuado")
    else:
        print("Nao é possivel efetuar o saque")
else:
    sys.exit("O sistema nao reconheceu seu tipo de conta, entre em contato com suporte.")
