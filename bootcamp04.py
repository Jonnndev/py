saldo = 1000
saque = 200
limite = 500
conta_especial = True



conta_normal_com_saldo_suficiente = (saque <= saldo and saque <= limite)
print(conta_normal_com_saldo_suficiente)
conta_especial_com_saldo_suficiente = (saque <= saldo and conta_especial )
