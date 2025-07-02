'''
Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar.
Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual 
como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.
'''

def acesso_escritorio():
    horas = int(input("Digite a hora atual sem os minutos (formato 24 horas): "))

    if horas < 0 or horas > 24:
        print("Entrada inválida! Verifique se as horas estão dentro do intervalo válido")
    elif 8 <= horas < 18:
        print("Acesso permitido. ")
    else: print("Acesso negado. ")

acesso_escritorio()