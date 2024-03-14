class SplitwiseService:
    def __init__(self, user_repository, expense_validator, expense_calculator, balance_repository):
        self.user_repository = user_repository
        self.expense_validator = expense_validator
        self.expense_calculator = expense_calculator
        self.balance_repository = balance_repository

    def add_expense(self,expense):
        if not self.expense_validator.validate(expense):
            raise ValueError("Invalid expense")
        
        shares = self.expense_calculator.calculate_shares(expense)
        self.balance_repository.update_balances(expense, shares)
        print("Expense added successfully")

    def show_balances(self,user_id=None):
        balances=self.balance_repository.get_balances(user_id)
        if balances:
            for balance in balances:
                print(balance)
        else:
            print("No balances found")