'''''
Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C.
No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos 
e não calcular o total.Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. 
Se algum valor for negativo, mostre uma mensagem informando o erro.
'''''
def tempo_projeto(a,b,c):
    if a <0 or b< 0 or c<0:
        print("Entrada inválida! Não existe dia negativo!! ")
    else:
        total= a + b +c
        print(f"As atividades levarão {total} de dias para serem concluidas! ")

tempo_projeto(1,3,-4)

