menu = """
[d] depositar
[s] sacar
[e] extrato
[q] sair

"""
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao =input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print("Operação falhou o valor informado é inválido: ")

    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = valor >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operação inválida o valor inserido é inválido: ")

        elif excedeu_limite:
            print("Limite de valor excedido.")
        
        elif excedeu_saques:
            print("limite de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            numero_saques +1

        else:
            print("ERRO")
    
    elif opcao == "e":
        print("================EXTRATO================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f'\nsaldo R${saldo:.2f}')
        print("=======================================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida porfavor digite outra opção")