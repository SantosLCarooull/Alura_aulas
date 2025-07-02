'''
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos
e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se 
ele ultrapassou o limite ou ainda está dentro do orçamento.
'''
def controle_gastos():
    gastos_mes = float(input("Digite o valor dos seus gastos mensais: R$ "))
    limite = 3000

    print(f"Seu gasto mensal é de R$ {gastos_mes} ")
    if gastos_mes > limite:
        print("Atenção! Você ultrapassou o limite do orçamento. ")
    else: print("Parabéns! Você está dentro do limite de gastos. ")

controle_gastos()