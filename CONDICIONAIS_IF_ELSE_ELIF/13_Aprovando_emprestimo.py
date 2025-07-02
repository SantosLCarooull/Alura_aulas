'''
Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:
    O valor da renda mensal precisa ser maior que R$ 2.000,00.
    O valor da parcela não pode ultrapassar 30% da renda.
Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. 
O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.
'''

def simula_emprestimo():
    renda=(float(input("Digite o valor da sua renda mensal: R$ ")))
    parcela=(float(input("Digite o valor desejado de parcela: R$ ")))

    lim_parc=renda * 0.3
    
    if renda > 2000 and parcela <= lim_parc:
        print("Empréstimo aprovado. ")
    else: print("Empréstimo recusado. ")

simula_emprestimo()




