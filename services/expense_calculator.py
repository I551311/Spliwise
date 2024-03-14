class ExpenseCalculator():
    def calculate_shares(self,expense):
        if expense["expense_type"] == "EQUAL":
            shares = {}
            amount_per_head = round(expense["amount"]/len(expense["participants"]),2)
            for participant in expense["participants"]:
                shares[participant] = amount_per_head
            return shares
        
        elif expense["expense_type"] == "EXACT":
            shares = {}
            for i in range(len(expense["participants"])):
                shares[expense["participants"][i]] = expense["values"][i]
            return shares
        
        elif expense["expense_type"] == "PERCENT":
            shares = {}
            for i in range(len(expense["participants"])):
                shares[expense["participants"][i]] = round((expense["values"][i]/100)*expense["amount"],2)
            return shares
        
        else:
            return {}