def main():
    from functions.menu import menu

    saldo = 0
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu(saldo, limite, numero_saques, LIMITE_SAQUES)

if __name__ == "__main__":
    main()