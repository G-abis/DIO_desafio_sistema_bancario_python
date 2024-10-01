menu = '''
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

->'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(f'Escolha uma opção:{menu}'))

    if opcao == 1:
        valor = float(input('Informe o valor de depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 2:
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Saldo insuficiente.')
        elif excedeu_limite:
            print('Operação falhou! Limite diário de saque atingido.')
        elif excedeu_saque:
            print('Operação falhou! Limite de números de saque atingido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Operação falhou! Valor informado é inválido.')
    elif opcao == 3:
        print('\n==================== EXTRAT0 ====================')
        print('Não foram realizadas operações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=================================================')
    elif opcao == 4:
        break
    else:
        print('Operação inválida! Escolha uma das opções acima.')