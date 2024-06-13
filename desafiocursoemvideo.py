salario = float(input("Qual valor do seu salario?"))
valor_do_emprestimo = float(input("Qual valor da casa (Emprestimo)?"))
parc_emprestimo = float(input("Em quantas parcelas voce deseja realizar o emprestimo?"))
prestacao_mensal = valor_do_emprestimo / parc_emprestimo

valor_max = salario*0.3
if prestacao_mensal <= valor_max:
    print("Emprestimo Aprovado")
else:
    print("Emprestimo Nao Aprovado")

