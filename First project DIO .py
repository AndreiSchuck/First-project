menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":

        print("\nDepósito\n")

        print("Insira o valor que deseja depositar: \n")

        valor_de_deposito = float(input())

        if valor_de_deposito > 0:

            saldo += valor_de_deposito
            extrato += f"Depósito: R$ {valor_de_deposito:.2f}\n" 

            print("\nDepósito realizado com sucesso!\n")

        else:

            print("O valor de deposito precisa ser diferente de 0!\n")

    elif opcao == "2":

        print("\nSaque --- Limite por saque de R$ 500,00\n")

        print("Insira o valor que deseja sacar: \n")

        valor_de_saque = float(input())

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor_de_saque > limite or valor_de_saque > saldo:

            print("\nO valor desejado excede o limite de saque ou saldo da conta\n")

        elif valor_de_saque <= limite and valor_de_saque <= saldo:

            saldo -= valor_de_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_de_saque:.2f}\n" 

            print("\nSaque realizado com sucesso!\n")

        elif excedeu_saques:

            print("Limite de saques por dia excedido!\n")

    elif opcao == "3":

        print("\nExtrato\n")

        print("Não foram realizadas operações na conta" if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == "4":

        break

    else:
        
        print("\nOpção inválida! Por favor selecione novamente a opção desejada \n")





