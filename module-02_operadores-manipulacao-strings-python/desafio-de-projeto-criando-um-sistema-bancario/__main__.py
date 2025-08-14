account_balance = 0.0
account_statement = ""
withdrawal_count = 0

# Constants
WITHDRAWAL_DAILY_LIMIT = 3
WITHDRAWAL_AMOUNT_LIMIT = 500.00

# System Messages
DISPLAY_OPTIONS = """
    Bem-vindo ao Sistema do Banco!!!
    
    Por favor, selecione a opção desejada...
        1. Depósito: digite a letra 'd'
        2. Saque:    digite a letra 's'
        3. Extrato:  digite a letra 'e'
        4. Sair:     digite a letra 'q'
"""
DEPOSIT_INPUT_INFO = "Digite o valor para depósito... R$"
DEPOSIT_INPUT_ERROR_MESSAGE = "O valor informado para depósito deve ser positivo."
WITHDRAWAL_INPUT_INFO = "Digite o valor para saque... R$"
EXIT_INFO = "Obrigado por usar o Sistema do Banco!!!"
INVALID_OPTION_ERROR_MESSAGE = "Opção inválida. Tente novamente."
WITHDRAWAL_NO_SUFFICIENT_FUNDS = "Sem fundos suficientes para o saque."
WITHDRAWAL_AMOUNT_OUT_OF_LIMIT = (
    f"Saque acima do valor limite máximo: R$ {WITHDRAWAL_AMOUNT_LIMIT}."
)
WITHDRAWAL_REQUEST_OUT_OF_LIMIT = (
    f"Limite de {WITHDRAWAL_DAILY_LIMIT} saques diários atingido."
)
WITHDRAWAL_INPUT_ERROR_MESSAGE = "O valor informado para saque deve ser positivo."

while True:

    user_input = input(DISPLAY_OPTIONS).casefold()

    if user_input == "d":
        user_input = input(DEPOSIT_INPUT_INFO)

        if user_input.isdecimal() and float(user_input) > 0.0:
            deposit_amount = float(user_input)
            account_balance += deposit_amount

            if account_statement:
                account_statement += "\n"
            account_statement += f"Depósito\tR$ {deposit_amount: .2f}".center(50)

            print("Depósito realizado com sucesso!")
        else:
            print(DEPOSIT_INPUT_ERROR_MESSAGE)

    elif user_input == "s":
        user_input = input(WITHDRAWAL_INPUT_INFO)

        if not user_input.isdecimal() or float(user_input) <= 0.0:
            print(WITHDRAWAL_INPUT_ERROR_MESSAGE)
            continue

        withdrawal_amount = float(user_input)

        if withdrawal_amount > account_balance:
            print(WITHDRAWAL_NO_SUFFICIENT_FUNDS)
        elif withdrawal_amount > WITHDRAWAL_AMOUNT_LIMIT:
            print(WITHDRAWAL_AMOUNT_OUT_OF_LIMIT)
        elif withdrawal_count == WITHDRAWAL_DAILY_LIMIT:
            print(WITHDRAWAL_REQUEST_OUT_OF_LIMIT)
        else:
            withdrawal_count += 1
            account_balance -= withdrawal_amount

            if account_statement:
                account_statement += "\n"
            account_statement += f"Saque\tR$ {withdrawal_amount: .2f}".center(50)

            print("Saque realizado com sucesso!")

    elif user_input == "e":
        print("")
        print("")
        print("Extrato conta".center(50))
        print("")
        print("Cliente - Conta atual".center(50))
        print("-----------------------------".center(50))
        print("Lançamentos".center(50))
        print("-----------------------------".center(50))
        print(account_statement)
        print(f"Saldo\tR$ {account_balance: .2f}".center(50))
        print("")
        print("Obrigado por usar o Sistema do Banco!!!".center(50))
        print("")
        print("")

    elif user_input == "q":
        print(EXIT_INFO)
        break

    else:
        print(INVALID_OPTION_ERROR_MESSAGE)
