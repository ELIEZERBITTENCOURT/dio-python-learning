saldo = 0
saques_diarios = 0
limite_saques_diarios = 3
limite_saque = 500

def exibir_menu():
    print("\nEscolha uma operação:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Consultar Extrato")
    print("4. Sair")

def depositar():
    global saldo
    valor_deposito = float(input("Digite o valor do depósito: R$ "))
    if valor_deposito > 0:
        saldo += valor_deposito
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. O depósito deve ser positivo.")

def sacar():
    global saldo, saques_diarios
    if saques_diarios < limite_saques_diarios:
        valor_saque = float(input("Digite o valor do saque: R$ "))
        if 0 < valor_saque <= saldo and valor_saque <= limite_saque:
            saldo -= valor_saque
            saques_diarios += 1
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
        else:
            print("Valor inválido. Verifique o saldo ou o limite de saque.")
    else:
        print("Limite diário de saques atingido.")

def exibir_extrato():
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print(f"Saques realizados hoje: {saques_diarios}")

while True:
    exibir_menu()
    opcao = input("Digite o número da operação desejada: ")
    if opcao == "1":
        depositar()
    elif opcao == "2":
        sacar()
    elif opcao == "3":
        exibir_extrato()
    elif opcao == "4":
        print("Obrigado por utilizar nosso sistema bancário!")
        break
    else:
        print("Opção inválida. Escolha novamente.")

