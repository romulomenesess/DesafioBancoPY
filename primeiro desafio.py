menu = """

[deposito] Depositar
[saque] Sacar
[extrato] Extrato
[sair] Sair

=> """

saldo = 0
extrato = ""
total_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

#DEPOSITO
    if opcao == "deposito":
        print("Selecionado: Depósito")
        valor_depositado = float(input("Digite o valor do depósito: "))

        if valor_depositado > 0:
            saldo += valor_depositado
            print("Foi depositado R$ " + str(valor_depositado) + " com sucesso!")
            extrato += f"Depósito: R$  {valor_depositado:.2f}\n"

        else: 
            print("Operação inválida! Tente novamente.")

#SAQUE
    elif opcao == "saque" and total_saques < 3:
        print("Selecionado: Saque")
        valor_sacado = float(input("Digite o valor a ser sacado: "))

        saque_maior_que_saldo = valor_sacado > saldo
        saque_maior__que_limite = valor_sacado > 500
        limite_de_saques = total_saques > LIMITE_SAQUE

        if  saque_maior_que_saldo:
            print("Saldo insuficiente! ")
        
        elif saque_maior_que_saldo: 
            print("Saque excedeu o limite de saque.")

        elif limite_de_saques:
            print("Limite diário de saque atingido!")

        elif valor_sacado > 0 and valor_sacado < 500:
            saldo -= valor_sacado
            print("Saque de R$ " + str(valor_sacado) + " efetuado com sucesso!")
            extrato += f"Saque: R$ {valor_sacado:.2f}\n"
            total_saques += 1
        
        else: 
            print("Operação inválida! Valor do saque deve ser igual ou inferior que R$ 500.")

#EXTRATO
    elif opcao == "extrato":
        print("Selecionado: Extrato ")
        print("_____________________EXTRATO_____________________")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\nSALDO: R$ {saldo:.2f}")
        print("________________________________________________")

#SAIR
    elif opcao == "Sair":
        break

    else: 
        print("Operação inválida, selecione um dos serviços acima.")