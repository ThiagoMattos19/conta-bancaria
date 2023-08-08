menu ="""
================BEM VINDO AO BANCO================
[d] depositar
[s] sacar
[e] extrato
[q] sair
==================================================
"""
saldo = 0
limite_saque = 500
extrato = ''
LIMITE_SAQUE = 3
numero_saques = 0

while True:
    opcao = input(menu).lower()
    if opcao == 'd':
        valor = float(input("Digite o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito R$:{valor:.2f}\n'
            print(f"Valor adicionado! seu saldo é {saldo}")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        
        limite_diario =  numero_saques >= LIMITE_SAQUE
       
        saque_limite = valor > limite_saque

        valor_insuficiente = valor > saldo
        
        if saque_limite:
            print("LIMITE DE SAQUES ATINGIDO")
        elif limite_diario:
            print("LIMITE DE SAQUES DIÁRIOS ATINGIDO")
        elif valor_insuficiente:
            print("VALOR INSUFICIENTE")
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Deposito R${valor:.2f}\n'
            numero_saques +=1
            print(f"VALOR SACADO SEU SALDO É {saldo}")

    elif opcao == "e":
        print("=========EXTRATO=========")
        print(f'seu extrato {extrato:.2f}\n' if not extrato else extrato)
        print(f"Seu Saldo atual {saldo:.2f}\n")
        print("=========================")
    elif opcao == "q":
        break
    else:
        print("Opção inválida! insira uma opção válida!")