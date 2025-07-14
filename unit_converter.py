# Importações
from lib import ui

# Função principal
while True:
    opções = [
        'Sair',
        'Temperatura'
    ]
    ui.menu(opções=opções, título='Conversor')
    resposta = int(input('Opção: '))

    if resposta == 0:
        print('Saindo... Volte Sempre!')
        break
    
    elif resposta == 1:
        from lib import temperature