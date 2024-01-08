def menu(saldo, limite, numero_saques, LIMITE_SAQUES):
    from .depositar import depositar
    from .extrato import extrato
    from .sacar import sacar
    
    print("""
____Conta Bancária____
[1] Sacar
[2] Depositar
[3] Extrato
[4] Sair\n
    """)

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        sacar(saldo, limite, numero_saques, LIMITE_SAQUES)
    elif opcao == 2:
        depositar(saldo, limite, numero_saques, LIMITE_SAQUES)
    elif opcao == 3:
        extrato(saldo, limite, numero_saques, LIMITE_SAQUES)
    else:
        print("Obrigado! Volte sempre!")
        input()