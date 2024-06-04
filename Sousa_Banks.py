valor_conta = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    print("""
            1 - Realizar depósito
            2 - Realizar saque
            3 - Consultar extrato
            0 - Encerrar programa
        """)

    opc = int(input("Opção escolhida: "))

    if opc == 0:
        exit()
    elif opc == 1:
        valor_deposito = float(input("Insira o valor para depósito: "))
        if valor_deposito > 0 :
            valor_conta += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Você deve inserir um valor positivo")

    elif opc == 2:
        valor_saque = float(input("Insira o valor de saque: "))
        if valor_saque <= 500:
            valor_conta -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
        elif valor_saque > 500 :
            print("Valor de saque não autorizado")
        else:
            print("Insira um valor válido para saque")

    elif opc == 3:
        print("\n----- EXTRATO -----")
        print("Não foram realizdas movimentações" if not extrato else extrato)
        print(f"Saldo: R$ {valor_conta:.2f}")
        
    else:
        print("Operação inválida!!")