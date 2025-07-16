# Importações
from lib import ui

# Função principal
while True:
    opções = [
        'Sair',
        'Temperatura',
        'Altura'
    ]
    ui.menu(opções=opções, título='Conversor')
    resposta = int(input('Opção: '))

    if resposta == 0:
        print('Saindo... Volte Sempre!')
        break
    
    elif resposta == 1:
        from lib import temperature

    elif resposta == 2:
        from lib import height

    else:
        print('\033[31mERRO! Selecione uma opção VÁLIDA!\033[m')
