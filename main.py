from repositories.balance_repository import BalanceRepository
from repositories.user_repository import UserRepository
from services import splitwise_service
from services.expense_calculator import ExpenseCalculator
from services.expense_validator import ExpenseValidator


def main():
    user_repository = UserRepository()
    expense_validator = ExpenseValidator()
    expense_calculator = ExpenseCalculator()
    balance_repository = BalanceRepository()
    splitwise = splitwise_service.SplitwiseService(user_repository, expense_validator, expense_calculator, balance_repository)

    while True:
        command = input("Enter command: ").split()
        if command[0] == "SHOW":
            if len(command) == 1:
                splitwise.show_balances()
            else:
                splitwise.show_balances(command[1])

        elif command[0] == "EXPENSE":
            _, payer_id, amount, no_of_users, *participants_expense = command
            expense = {
                "payer_id": command[1],
                "amount": float(command[2]),
                "no_of_users": command[3],
                "participants": command[4:4+int(command[3])],
                "expense_type": command[4+int(command[3])],
                "values": command[5+int(command[3]):] if command[4+int(command[3])] != "EQUAL" else []
            }
            print(expense)
            splitwise.add_expense(expense)    

if __name__ == "__main__":
    main()