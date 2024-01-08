def depositar(saldo, limite, numero_saques, LIMITE_SAQUES):
    from .menu import menu
    
    valor = float(input("\nDigite o valor do deposito: "))

    saldo += valor

    print("\nR$f{valor} depositado com sucesso!")

    menu(saldo, limite, numero_saques, LIMITE_SAQUES)