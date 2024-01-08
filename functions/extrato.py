def extrato(saldo, limite, numero_saques, LIMITE_SAQUES):
    from .menu import menu
    
    saldo = saldo
    print(""" 
\nExtrato:
    Saldo em conta: f{saldo}
............................
    """)

    menu(saldo, limite, numero_saques, LIMITE_SAQUES)