saque = float(input("Qual valor deseja sacar?"))
saldo = 300
status = "Sucesso" if saldo >= saque else "falha"
print(f"{status} ao realizar o saque")