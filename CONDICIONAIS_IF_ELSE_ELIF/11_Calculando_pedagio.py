'''
Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:
    Até 100 km: R$ 10,00
    Entre 100 km e 200 km: R$ 20,00
    Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.
'''

def calc_pedagio():
    distancia=(float(input("Digite a distância percorrida em KM: ")))

    if distancia <= 100:
        print("Você pagará R$ 10,00 de pedágio. ")
    elif distancia >100 and distancia <200:
        print("Você pagará R$ 20,00 de pedágio. ")
    else: print("Você pagará R$ 30,00 de pedágio. ")

calc_pedagio()