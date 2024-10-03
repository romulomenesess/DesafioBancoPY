import textwrap

def menu():
    menu = """\n

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [cc] Criar conta
    [gu] Gerar usuário
    [lc] Listar contas
    => """
    return input(menu)

def depositar(saldo, valor,extrato, /): 
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
                print("Operação falhou! O valor informado é inválido.")

def sacar(*, valor, saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def imprimir_extrato(saldo, /, *, extrato,):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def gerar_usuario(usuarios):
    cpf = input("Digite o seu CPF(somente números):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Este CPF já está cadastrado!")
        return
    nome = input("Informe o seu nome completo: ")
    nascimento = input("Digite a sua data de nascinmento. Exemplo: (dd/mm/aaaa): ")
    endereco = input("Digite o seu endereço. Exemplo: (logradouro, nro, bairro, cidade/estado): ")

    usuarios.append["nome": nome, "cpf": cpf, "data_nascimento": nascimento, "endereco": endereco]
    print("Um novo usuário foi cadastrado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario[cpf] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_da_conta, usuarios):
    cpf = input("Informe o CPF do usuário")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_da_conta, "usuario": usuario}
    else:
        print("Infelizmente ocorreu um erro na criação da sua conta. Tente novamente!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            Numero da Conta: \t\t{conta['numero_conta']}
            Titular da Conta:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def principal():
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar()

        elif opcao == "s":
            sacar()

        elif opcao == "e":
            imprimir_extrato()

        elif opcao == "gu":
            gerar_usuario(usuarios)

        elif opcao == "cc":
            numero_da_conta = len(contas) +  1
            conta = criar_conta(AGENCIA, numero_da_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
             listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

principal()