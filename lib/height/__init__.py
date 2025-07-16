# Importações
from lib import ui

opções = [
    'Voltar',
    'Metro',
    'Centímetro',
    'Pé',
    'Polegada'
]

while True:
    ui.menu(opções, 'Altura')
    resposta1 = int(input('De qual altura quer converter? '))

    if resposta1 == 0:
        print('Voltando...')
        break

    else:
        converter = opções[resposta1]
        resposta2 = int(input('Para qual altura quer converter? '))

        if resposta1 == resposta2:
            print('\033[33mAs unidades de origem e destino são iguais. Nenhuma conversão necessária.\033[m')
        
        else:
            conversão = float(input(f'Digite a altura em {opções[resposta1]}: '))
            if resposta1 == 1:
                if resposta2 == 2:
                    convertido = conversão * 100

                elif resposta2 == 3:
                    convertido = conversão * 3.281

                elif resposta2 == 4:
                    convertido = conversão * 39.37

            elif resposta1 == 2:
                if resposta2 == 1:
                    convertido = conversão / 100

                elif resposta2 == 3:
                    convertido = conversão / 30.48

                elif resposta2 == 4:
                    convertido = conversão / 2.54

            elif resposta1 == 3:
                if resposta2 == 1:
                    convertido = conversão / 3.281

                elif resposta2 == 2:
                    convertido = conversão * 30.48

                elif resposta2 == 4:
                    convertido = conversão * 12

            elif resposta1 == 4:
                if resposta2 == 1:
                    convertido = conversão / 39.37

                elif resposta2 == 2:
                    convertido = conversão * 2.54

                elif resposta2 == 3:
                    convertido = conversão / 12

            else:
                print('\033[31mERRO! Digite uma opção válida.\033[m')

            print(f'{convertido}'.replace('.', ','))
