# Importações
from lib import ui

opções = [
    'Voltar',
    'Km/h',
    'm/s',
    'mph',
    'pé/s',
    'nó'
]

while True:
    ui.menu(opções, 'Velocidades')
    resposta1 = int(input(f'De qual velocidade quer converter? '))

    if resposta1 == 0:
        print('Voltando...')
        break

    else:
        converter = opções[resposta1]
        resposta2 = int(input('Para qual velocidade quer converter? '))

        if resposta1 == resposta2:
            print('\033[33mAs unidades de origem e destino são iguais. Nenhuma conversão necessária.\033[m')
        
        else:
            conversão = float(input(f'Digite a altura em {opções[resposta1]}: '))
            if resposta1 == 1:
                if resposta2 == 2:
                    convertido = conversão / 3.6

                elif resposta2 == 3:
                    convertido = conversão / 1.609

                elif resposta2 == 4:
                    convertido = conversão / 1.097

                elif resposta2 == 5:
                    convertido = conversão / 1.852

            elif resposta1 == 2:
                if resposta2 == 1:
                    convertido = conversão * 3.6

                elif resposta2 == 3:
                    convertido = conversão * 2.237

                elif resposta2 == 4:
                    convertido = conversão * 3.281

                elif resposta2 == 5:
                    convertido = conversão * 1.944

            elif resposta1 == 3:
                if resposta2 == 1:
                    convertido = conversão * 1.609

                elif resposta2 == 2:
                    convertido = conversão / 2.237

                elif resposta2 == 4:
                    convertido = conversão * 1.467

                elif resposta2 == 5:
                    convertido = conversão / 1.151

            elif resposta1 == 4:
                if resposta2 == 1:
                    convertido = conversão * 1.097

                elif resposta2 == 2:
                    convertido = conversão / 3.281

                elif resposta2 == 3:
                    convertido = conversão / 1.467

                elif resposta2 == 5:
                    convertido = conversão / 1.688

            elif resposta1 == 5:
                if resposta2 == 1:
                    convertido = conversão * 1.652

                elif resposta2 == 2:
                    convertido = conversão / 1.944

                elif resposta2 == 3:
                    convertido = conversão * 1.151

                elif resposta2 == 4:
                    convertido = conversão * 1.688

            else:
                print('\033[31mERRO! Digite uma opção válida.\033[m')

            print(f'{convertido}'.replace('.', ','))
