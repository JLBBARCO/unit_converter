# Importações
from lib import ui

opçõesTemperatura = [
            'Voltar',
            'Celsius',
            'Fahrenheit',
            'Kelvin'
        ]
while True:
    ui.menu(opções=opçõesTemperatura, título='Temperatura')
    resposta1 = int(input('De qual medida quer converter? '))

    if resposta1 == 0:
        print('Saindo do conversor...')
        break
    
    else:
        resposta2 = int(input('Para qual medida quer converter? '))

        if resposta1 == 1:
            if resposta2 == 0:
                break

            elif resposta2 == 1:
                print('\033[33mAs unidades de origem e destino são iguais. Nenhuma conversão necessária.\033[m')
                
            elif resposta2 == 2:
                conversão = float(input('Digite a temperatura em Celsius: '))
                resultado = (conversão * 9/5) + 32
                print(f"A temperatura em Fahrenheit é: {resultado:.2f} °F")

            elif resposta2 == 3:
                conversão = float(input('Digite a temperatura em Celsius: '))
                resultado = conversão + 273.15
                print(f"A temperatura em Kelvin é: {resultado:.2f} K")
                
            else:
                print('\033[31mERRO! Digite uma opção válida.\033[m')
            continue

        elif resposta1 == 2:
            if resposta2 == 0:
                break

            elif resposta2 == 1:
                conversão = float(input('Digite a temperatura em Fahrenheit: '))
                resultado = (conversão - 32) * 5/9
                print(f"A temperatura em Celsius é: {resultado:.2f} °C")
                
            elif resposta2 == 2:
                print('\033[33mAs unidades de origem e destino são iguais. Nenhuma conversão necessária.\033[m')
                
            elif resposta2 == 3:
                conversão = float(input('Digite a temperatura em Fahrenheit: '))
                resultado = (conversão - 32) * 5/9 + 273.15
                print(f"A temperatura em Kelvin é: {resultado:.2f} K")
                
            else:
                print('\033[31mERRO! Digite uma opção válida.\033[m')
            continue

        elif resposta1 == 3:
            if resposta2 == 0:
                break

            elif resposta2 == 1:
                conversão = float(input('Digite a temperatura em Kelvin: '))
                resultado = conversão - 273.15
                print(f"A temperatura em Celsius é: {resultado:.2f} °C")

            elif resposta2 == 2:
                conversão = float(input('Digite a temperatura em Kelvin: '))
                resultado = (conversão - 273.15) * 9/5 + 32
                print(f"A temperatura em Fahrenheit é: {resultado:.2f} °F")

            elif resposta2 == 3:
                print('\033[33mAs unidades de origem e destino são iguais. Nenhuma conversão necessária.\033[m')

            else:
                print('\033[31mERRO! Digite uma opção válida.\033[m')
            continue

        else:
            print('\033[31mERRO! Digite uma opção válida.\033[m')
            continue
