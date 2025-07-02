'''''
Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. 
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.
'''''
def controle_temp():
    temp_atual=float(input("Digite a temperatura atual: "))

    if temp_atual > 25:
        print("Alerta! Temperatura acima do limite permitido. ")
    else: print(f"Temperatura de {temp_atual} °C está dentro do limite seguro.")

controle_temp()