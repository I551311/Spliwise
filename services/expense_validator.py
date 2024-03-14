class ExpenseValidator():
    def validate(self,expense):
        print(expense)
        if expense["expense_type"] == "EQUAL":
            return True
        
        elif expense["expense_type"] == "EXACT":
            return sum(expense["values"]) == expense["amount"]
        
        elif expense["expense_type"] == "PERCENT":
            return sum(expense["values"]) == 100
        
        else:
            return False
