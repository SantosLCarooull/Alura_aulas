'''
Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar. 
Essa verificação será usada para definir ações diferentes dentro do jogo. Escreva um programa que receba um 
número inteiro e exiba uma mensagem informando se ele é par ou ímpar.
'''

def paridade_num():
    num=(int(input("Digite um número inteiro: ")))
    verificador= num % 2

    if num == 0:
        print("O número é par. ")
    else: print("O número é ímpar. ")

paridade_num()