menu = """
[d] deposito    
[s] saque
[e] extrato 
[q] sair 
"""
saldo = 0
LIMITE_SAQUES = 3
valor_limite = 500
numero_saques = 0
extrato = ''

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito {valor:.2f}\n'
            print(f"valor depositado! agora seu saldo é {saldo}")

    elif opcao == "s":
         valor = float(input("Digite o valor do saque: "))
        
         excedeu_saldo = valor > saldo

         excedeu_limite = valor > valor_limite

         excedeu_limite_diario = numero_saques >= LIMITE_SAQUES
         
       
         if excedeu_saldo:
             print('você não tem esse valor em sua conta')

         elif excedeu_limite_diario:
             print("numero de saques diários atingido!")
        
         elif excedeu_limite:
             print(f"Você excedeu o limite de valor de saque o valor limite é {valor_limite}")

         elif valor > 0:
            saldo -= valor
            extrato += f'saque: {valor:.2f}\n'
            numero_saques +=1
            print(f"valor sacado! agora seu saldo é {saldo}")

         else:
             print("Erro")

    elif opcao == "e":
        print("==============EXTRATO==============")
        print(f'seu extrato {extrato:.2f}' if not extrato else extrato)
        print(f'\nSaldo R$:{saldo:.2f}')
        print('===================================')

    elif opcao == "q":
        break
    else:
        print("OPÇÃO INVÁLIDA. PORFAVOR INSIRA UMA OPÇÃO VÁLIDA")
        