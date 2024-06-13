import sys

opcao = -1
extrato = 500
saques_realizados = [0, 0, 0]
numero_saques = 0
total_saques = 0

print("""
-----------------------------------
                                  /  
    Banco JOLA                   /
                                /
--------------------------------
""")

while opcao != 0:
    opcao = int(input("ESCOLHA A FUNCIONALIDADE [1]SAQUE [2]DEPOSITO [3]VISUALIZAR EXTRATO [0]SAIR DO BANCO: "))

    if opcao == 1:
        if numero_saques >= 3:
            print("Você atingiu o limite máximo de 3 saques por dia.")
            continue

        valor_saque = float(input("Qual valor deseja sacar? "))

        if valor_saque <= extrato and valor_saque <= 500 and (total_saques + valor_saque) <= 1500:
            extrato -= valor_saque
            saques_realizados[numero_saques] = valor_saque
            numero_saques += 1
            total_saques += valor_saque
            print("Saque efetuado")
        else:
            print("Saque não foi possível por falta de fundos ou excedeu os limites permitidos.")

    elif opcao == 2:
        deposito = float(input("Qual valor de depósito? "))

        if deposito > 0:
            extrato += deposito
            print("Depósito efetuado")
        else:
            print("Depósito não foi possível")

    elif opcao == 3:
        print(f"O valor do seu extrato é de {extrato}")
        if numero_saques > 0:
            for saques in range(numero_saques):
                print(f"{saques + 1}º saque no valor de: {saques_realizados[saques]}")
        else:
            print("Nenhum saque realizado no dia.")

sys.exit("Opçao nao encontrada")
