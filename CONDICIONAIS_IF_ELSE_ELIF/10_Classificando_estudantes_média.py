'''
Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram
de recuperação ou reprovados. As regras são:
    Média >= 7: Aprovado
    5 <= Média < 7: Recuperação
    Média < 5: Reprovado
Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.
'''

def media_aluno():
    notas = []

    for i in range(3):
        atividade=(float(input(f"Digite da atividade {i+1}: ")))
        notas.append(atividade)

    media=round(sum(notas)/len(notas))
    print(f"A média final é: {media}")

    if media >= 7:
        print("Aluno aprovado. ")
    elif 5 <= media < 7:
        print("Aluno em recuperação. ")
    else: print("Aluno reprovado. ")

media_aluno()