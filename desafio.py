menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            print(f"Depósito: R${valor:.2f}")
        
        else:
            print("Operação falhou! Valor inválido.")
    
    elif opcao == 2:
        valor = float(input("Digite o valor do saque: "))

        if valor <= 0:
            print("Operação falhou! Valor inválido")
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente")
        elif numero_saques > LIMITE_SAQUES:
            print("Operação falhou! Limite saques ultrapassado")
        elif valor > limite:
            print(f"Operação falhou! Limite ultrapassado.\nLimite atual: {limite}")
        else:
            saldo -= valor
            numero_saques += 1
            print(f"""
                    Saque: R${valor:.2f}
                    Número Saques restantes: {LIMITE_SAQUES - numero_saques}
                """)
    
    elif opcao == 3:
        print(f"""
                Saldo: R${saldo:.2f}
                Número Saques restantes: {LIMITE_SAQUES - numero_saques}
            """)
    else:
        break
