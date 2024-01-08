def sacar(saldo, limite, numero_saques, LIMITE_SAQUES):
    from .menu import menu
    valor = float(input("\nDigite o valor do saque: "))

    if valor < saldo and numero_saques < LIMITE_SAQUES and valor > limite:
        saldo -= valor
        numero_saques += 1
        print("R$f{valor} retirado com sucesso!")
        menu(saldo, limite, numero_saques, LIMITE_SAQUES)
    elif valor < saldo:
        print("Operação falhou! Saldo Insuficiente")
        menu(saldo, limite, numero_saques, LIMITE_SAQUES)
    elif valor > limite:
        print("Operação falhou! Valor superior ao limite")
        menu(saldo, limite, numero_saques, LIMITE_SAQUES)
    else: 
        print("Operação falhou! Limite de saques atingido")
        menu(saldo, limite, numero_saques, LIMITE_SAQUES)